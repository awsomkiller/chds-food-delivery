import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import OrderSerializer
from .models import Orders
from django.db import transaction as db_transaction
from apps.transactions.models import Transaction, Wallet
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


class OrderCreateView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        try:
            if serializer.is_valid(raise_exception=True):
                order = serializer.save()
                transaction = Transaction.objects.create(
                    user=order.user,
                    amount=order.amount,
                    currency='aud',
                    order_type='FOOD_ORDER',
                    transaction_from='STRIPE',
                    operation_type='DEBIT',
                )
                payment_intent = stripe.PaymentIntent.create(
                    amount=int(float(order.amount) * 100),
                    currency='aud',
                    metadata={'order_id': order.order_id, 'user_id': order.user.id},
                )
                transaction.stripe_payment_intent_id = payment_intent['id']
                transaction.status = payment_intent['status']
                transaction.save()
                order.transaction = transaction
                order.status = "ORDER_PLACED"
                order.save()
                return Response({
                    "order_id": order.order_id,
                    "client_secret": payment_intent['client_secret']
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
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error(f"Invalid signature: {e}")
        return HttpResponse(status=400)

    event_type = event['type']
    data_object = event['data']['object']

    if event_type in ['payment_intent.succeeded', 'payment_intent.payment_failed']:
        payment_intent = data_object
        payment_status = payment_intent['status']
        transaction_id = payment_intent['id']  # Stripe Payment Intent ID
        order_id = payment_intent['metadata'].get('order_id')  # May be None for wallet recharge
        wallet_id = payment_intent['metadata'].get('wallet_id')  # Assuming wallet recharge includes wallet_id

        try:
            # Retrieve the Transaction based on Stripe Payment Intent ID
            transaction = Transaction.objects.get(stripe_payment_intent_id=transaction_id)
        except Transaction.DoesNotExist:
            logger.warning(f"Transaction with Payment Intent ID {transaction_id} does not exist.")
            return HttpResponse(status=200)  # Return 200 to Stripe to acknowledge receipt

        # Start an atomic transaction to ensure data integrity
        with db_transaction.atomic():
            # Update Transaction status and related fields
            transaction.status = payment_status
            try:
                charge = payment_intent['charges']['data'][0]
                transaction.stripe_charge_id = charge['id']
                transaction.payment_method = charge['payment_method_details']['type']
                transaction.payment_method_details = charge['payment_method_details']
                transaction.receipt_url = charge.get('receipt_url')
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
                    if event_type == 'payment_intent.succeeded':
                        order.status = "PAYMENT_SUCCESS"
                    elif event_type == 'payment_intent.payment_failed':
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
                    if event_type == 'payment_intent.succeeded':
                        # Update Wallet Balance
                        wallet.balance += transaction.amount
                        wallet.save()
                        logger.info(f"Wallet {wallet_id} recharged by {transaction.amount}. New balance: {wallet.balance}.")
                    elif event_type == 'payment_intent.payment_failed':
                        # Optionally, you can notify the user or take other actions
                        logger.info(f"Wallet recharge failed for Wallet ID {wallet_id}.")
            else:
                logger.warning(f"Unknown order_type {transaction.order_type} for Transaction ID {transaction.id}.")

    else:
        # Handle other event types if necessary
        logger.info(f"Unhandled event type: {event_type}")

    return HttpResponse(status=200)