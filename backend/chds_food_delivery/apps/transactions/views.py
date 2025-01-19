from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from apps.transactions.models import Transaction,WalletCoupon,OrderCoupon
from apps.transactions.serializers import (
    TransactionSerializer ,
    WalletCouponSerializer,
    OrderCouponSerializer,
    ListWalletSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Q

from .models import Transaction, Wallet
from .serializers import WalletRechargeSerializer

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


class TransactionViewSet(ModelViewSet):
    http_method_names = ['get','post',"delete"]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset =  self.queryset.filter(user=self.request.user)
        return queryset
    

class WalletCouponViewSet(ReadOnlyModelViewSet):
    queryset = WalletCoupon.objects.filter(is_active=True)
    serializer_class = WalletCouponSerializer
              

class OrderCouponViewSet(ReadOnlyModelViewSet):
    queryset = OrderCoupon.objects.filter(is_active=True)
    serializer_class = OrderCouponSerializer
    permission_classes =  []
        

class WalletRechargeView(APIView):
    """
    API view to handle wallet recharge requests.
    """
    serializer_class = WalletRechargeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        try:
            if serializer.is_valid(raise_exception=True):
                amount = serializer.validated_data['amount']
                wallet, created = Wallet.objects.get_or_create(user=request.user)

                transaction = Transaction.objects.create(
                    user=request.user,
                    amount=amount,
                    currency='aud',
                    order_type='WALLET_RECHARGE',
                    transaction_from='STRIPE',
                    operation_type='CREDIT',
                )

                payment_intent = stripe.PaymentIntent.create(
                    amount=int(float(amount) * 100),
                    currency='aud',
                    payment_method_types=["card","alipay", "wechat_pay"],
                    metadata={
                        'transaction_id': transaction.transaction_id,
                        'user_id': request.user.id,
                        "wallet_id":wallet.wallet_id,
                    },
                )

                transaction.stripe_payment_intent_id = payment_intent['id']
                transaction.status = payment_intent['status']
                print(payment_intent)
                transaction.save()

                # if payment_intent['status'] == 'succeeded':
                #     wallet, created = Wallet.objects.get_or_create(user=request.user)
                #     wallet.balance += amount
                #     wallet.save()

                return Response({
                    "transaction_id": transaction.transaction_id,
                    "client_secret": payment_intent['client_secret']
                }, status=status.HTTP_201_CREATED)

        except stripe.error.CardError as e:
            return Response({"message": "Card declined.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.RateLimitError as e:
            return Response({"message": "Rate limit error.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.InvalidRequestError as e:
            return Response({"message": "Invalid request.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.AuthenticationError as e:
            return Response({"message": "Authentication error.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.APIConnectionError as e:
            return Response({"message": "Network error.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.StripeError as e:
            return Response({"message": "Stripe error occurred.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({
                "message": "An error occurred during the wallet recharge.",
                "error": str(exc).strip("\n")
            }, status=status.HTTP_400_BAD_REQUEST)
        

class WalletTransactionsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get(self, request):
        instances = Transaction.objects.filter(Q(user=request.user) & (Q(transaction_from="WALLET") | Q(order_type="WALLET_RECHARGE")))
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class WalletViewSet(ModelViewSet):
    """
    API endpoint for managing wallets.
    """
    http_method_names=['get',"options"]
    queryset = Wallet.objects.all()
    serializer_class = ListWalletSerializer

    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
