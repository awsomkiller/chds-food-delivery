import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import OrderSerializer,ListOrdersSerilaizer
from .models import Orders
from django.db import transaction as db_transaction
from apps.transactions.models import Transaction, Wallet
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import logging
from apps.restaurants.models import DeliveryPoint,PickupLocation
from rest_framework.generics import ListAPIView

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


class OrderCreateView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def _make_transaction(self,order,payment_method):
        transaction = Transaction.objects.create(
                    user=order.user,
                    amount=order.amount,
                    currency='aud',
                    order_type='FOOD_ORDER',
                    transaction_from=payment_method,
                    operation_type='DEBIT',
                )
        return transaction
    
 
    def _make_payment_from_wallet(self,amount):
        instance  = self.request.user.digital_wallet
        instance.withdraw(amount)
    
    def _check_payment_method(self,data):
        copy_data = data.copy()
        payment_method = copy_data.pop("payment_type")
        if payment_method and payment_method == "wallet":
            return copy_data,"wallet"
        return copy_data,"stripe"
        
    def _update_instances(self,order,transaction,transaction_status):
        transaction.status = transaction_status
        transaction.save()
        order.transaction = transaction
        order.status = "ORDER_PLACED"
        order.save()
        
    def calculate_charges(self,amount):
        if not amount > 0:
            raise "Amount must be Valid Positive Integer"
        return (amount*10)/100
        
        
    def add_charges(self,data):
        if data['order_type'] == "PICKUP":
            pickup_location  = data.get("pickup_location")
            pickup_instance = PickupLocation.objects.get(id=pickup_location)
            if not pickup_instance:
                raise "Pickup location Not Found"
            shipping_charges = pickup_instance.price
            total_product_price = shipping_charges + data['amount']
            tax_charges = self.calculate_charges(total_product_price)
           
        elif data['order_type'] == "DELIVERY":
            delivery_location = data.get("delivery_location")
            delivery_instance = DeliveryPoint.objects.get(id=delivery_location)  
            if not delivery_instance:
                raise "Delivery location Not Found"
            shipping_charges = delivery_instance.price 
            total_product_price =shipping_charges + data['amount']
            tax_charges = self.calculate_charges(total_product_price)
        else:
            raise "Unknown Order Type"
        
        data['shipping_charges'] = str(shipping_charges)
        data['total_price'] =  str(total_product_price + tax_charges)
        return data
        
    
    def post(self, request, *args, **kwargs):
        try:
            data , payment_method = self._check_payment_method(request.data)
            data = self.add_charges(data)
            serializer = self.serializer_class(data=data, context={'request':request})
            if serializer.is_valid(raise_exception=True):
                order = serializer.save()
                
                if payment_method =="stripe":
                    transaction = self._make_transaction(order,"STRIPE")
                    payment_intent = stripe.PaymentIntent.create(
                        amount=int(float(order.total_price) * 100),
                        currency='aud',
                        payment_method_types=["card","alipay", "wechat_pay"],
                        metadata={'order_id': order.order_id, 'user_id': order.user.id},
                    )
                    transaction.stripe_payment_intent_id = payment_intent['id']
                    transaction_status = payment_intent['status']
                    self._update_instances(order,transaction,transaction_status)
                    return Response({
                        "order_id": order.order_id,
                      "client_secret": payment_intent['client_secret']
                    }, status=status.HTTP_201_CREATED)
                    
                elif payment_method =="wallet":
                    transaction = self._make_transaction(order,"WALLET")
                    self._make_payment_from_wallet(int(float(order.total_price)))
                    transaction_status = "succeeded"
                    self._update_instances(order,transaction,transaction_status)
                    return Response({
                        "order_id": order.order_id,
                    }, status=status.HTTP_201_CREATED)
                       
        except Exception as exc:
            return Response({"message": "error occurred", "error": str(exc).strip("\n")}, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        logger.error(f"Invalid payload: {e}")
        return JsonResponse({"error":str(e)},status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error(f"Invalid signature: {e}")
        return JsonResponse({"error":str(e)},status=400)

    event_type = event['type']
    data_object = event['data']['object']
    
    if event_type in ["charge.succeeded","charge.failed"]:
        charge_id = data_object['id']
        payment_intent_id = data_object['payment_intent']
        payment_method_id = data_object['payment_method']
        metadata = data_object['metadata']
        order_id = metadata.get('order_id')
        wallet_id = metadata.get('wallet_id')
        status = data_object['status']
        receipt_url=data_object['receipt_url']
        payment_method_details=data_object['payment_method_details']
        
        try:
            # Retrieve the Transaction based on Stripe Payment Intent ID
            transaction = Transaction.objects.get(stripe_payment_intent_id=payment_intent_id)
        except Transaction.DoesNotExist:
            logger.warning(f"Transaction with Payment Intent ID {payment_intent_id} does not exist.")
            return HttpResponse(status=200)  
      
    
            # Start an atomic transaction to ensure data integrity
        with db_transaction.atomic():
            # Update Transaction status and related fields
            transaction.status = status
            try:
                transaction.stripe_charge_id = charge_id
                transaction.payment_method = payment_method_details['type']
                transaction.payment_method_details = payment_method_details
                transaction.receipt_url = receipt_url
            except (IndexError, KeyError) as e:
                logger.error(f"Error retrieving charge details: {e}")

            transaction.save()

            # Determine the type of transaction and process accordingly
            if transaction.order_type == 'FOOD_ORDER':
                # Handle E-commerce Order
                try:
                    order = Orders.objects.get(order_id=order_id)
                except Orders.DoesNotExist:
                    logger.warning(f"Order with ID {order_id} does not exist.")
                    order = None

                if order:
                    if event_type == 'charge.succeeded':
                        order.status = "PAYMENT_SUCCESS"
                    elif event_type == 'charge.failed':
                        order.status = "PAYMENT_FAILED"
                    order.save()
                    logger.info(f"Order {order_id} status updated to {order.status}.")
                    
            elif transaction.order_type == 'WALLET_RECHARGE':
                # Handle Wallet Recharge
                try:
                    wallet = Wallet.objects.get(wallet_id=wallet_id)
                except Wallet.DoesNotExist:
                    logger.warning(f"Wallet with ID {wallet_id} does not exist.")
                    wallet = None

                if wallet:
                    wallet.deposit(transaction.amount)
                    logger.info(f"Wallet {wallet_id} recharged by {transaction.amount}. New balance: {wallet.balance}.")    
            else:
                logger.warning(f"Unknown order_type {transaction.order_type} for Transaction ID {transaction.id}.")          
    else:
        # Handle other event types if necessary
        logger.info(f"Unhandled event type: {event_type}")

    return JsonResponse({"message":"success"},status=200)


class ListOrders(ListAPIView):
    serializer_class=ListOrdersSerilaizer
    pagination_class=None
    
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user).order_by("-id")[:10]