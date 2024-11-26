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
from apps.transactions.models import Transaction
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_id = payment_intent['metadata'].get('order_id')
        try:
            transaction = Transaction.objects.get(stripe_payment_intent_id=payment_intent['id'])
            transaction.status = payment_intent['status']
            charge = payment_intent['charges']['data'][0]
            transaction.stripe_charge_id = charge['id']
            transaction.payment_method = charge['payment_method_details']['type']
            transaction.payment_method_details = charge['payment_method_details']
            transaction.receipt_url = charge.get('receipt_url')
            transaction.save()

            order = Orders.objects.get(order_id=order_id)
            order.status = "PAYMENT_SUCCESS"
            order.save()
        except Transaction.DoesNotExist:
            pass
        except Orders.DoesNotExist:
            pass

    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        order_id = payment_intent['metadata'].get('order_id')
        try:
            transaction = Transaction.objects.get(stripe_payment_intent_id=payment_intent['id'])
            transaction.status = payment_intent['status']
            transaction.save()

            order = Orders.objects.get(order_id=order_id)
            order.status = "PAYMENT_FAILED"
            order.save()
        except Transaction.DoesNotExist:
            pass
        except Orders.DoesNotExist:
            pass

    return HttpResponse(status=200)