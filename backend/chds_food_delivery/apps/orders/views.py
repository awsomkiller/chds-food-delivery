import stripe
from decimal import Decimal
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import OrderSerializer,ListOrdersSerilaizer
from .models import Orders
from apps.transactions.models import OrderCoupon
from django.db import transaction as db_transaction
from apps.transactions.models import Transaction, Wallet
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import logging
from rest_framework.generics import ListAPIView
from .utilities import process_menu_item_cost, get_shipping_charge, calculate_discount
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


class OrderCreateView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def _make_transaction(self,order,payment_method):
        transaction = Transaction.objects.create(
            user=order.user,
            amount=order.total_price,
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
        payment_method = data.pop("payment_type")
        return data, payment_method
        
    def _update_instances(self,order,transaction,transaction_status):
        transaction.status = transaction_status
        transaction.save()
        order.transaction = transaction
        order.status = "ORDER_PLACED"
        order.save()
        
    def calculate_total_charges(self, data):
        shipment = data.get('shipping_charges', 0)
        subtotal = data.get('amount', 0) 
        discount = data.get('discount', 0)
        total = float(shipment) + float(subtotal) - float(discount)
        total_price = total + (total * 10 / 100)
        data['total_price'] = total_price
        return data
        
    def calculate_subtotal(self, data):
        subtotal = 0
        menu_item = json.loads(data.get('menu_item'))
        for item in menu_item:
            subtotal += process_menu_item_cost(item)
        data['amount'] = subtotal
        return data

    def calculate_shipment_charge(self, data):
        shipping_charge = get_shipping_charge(data)
        data['shipping_charges'] = str(shipping_charge)
        return data

    def check_for_coupons(self, data):
        try:
            coupon_code = data.pop('coupon')
            coupon = OrderCoupon.objects.get(code=coupon_code, is_active=True)
            discount = calculate_discount(data, coupon)
            data['discount'] = discount
            data['coupon'] = coupon
            return data

        except Exception as e:
            data['coupon'] = None
            return data
               
    
    def post(self, request, *args, **kwargs):
        try:
            data , payment_method = self._check_payment_method(request.data)
            data = self.calculate_subtotal(data)
            data = self.check_for_coupons(data)
            data = self.calculate_shipment_charge(data) 
            data = self.calculate_total_charges(data)
            serializer = self.serializer_class(data=data, context={'request':request})
            if serializer.is_valid(raise_exception=True):
                order = serializer.save()
                
                if payment_method =="wallet":
                    transaction = self._make_transaction(order,"WALLET")
                    self._make_payment_from_wallet(order.total_price)
                    transaction_status = "succeeded"
                    self._update_instances(order,transaction,transaction_status)
                    return Response({
                        "order_id": order.order_id,
                    }, status=status.HTTP_201_CREATED)
            
                else:
                    transaction = self._make_transaction(order,"STRIPE")
                    payment_intent = stripe.PaymentIntent.create(
                        amount=(float(order.total_price) * 100),
                        currency='aud',
                        payment_method_types=["card", "alipay", "wechat_pay"],
                        metadata={'order_id': order.order_id, 'user_id': order.user.id},
                    )
                    transaction.stripe_payment_intent_id = payment_intent['id']
                    transaction_status = payment_intent['status']
                    self._update_instances(order,transaction,transaction_status)
                    return Response({
                        "order_id": order.order_id,
                      "client_secret": payment_intent['client_secret']
                    }, status=status.HTTP_201_CREATED)
                       
        except Exception as exc:
            print(exc)
            return Response({"message": "error occurred", "error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        
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