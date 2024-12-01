from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.transactions.views import (
    TransactionViewSet,
    WalletRechargeView,
    WalletTransactionsView,WalletViewSet
    )

router = DefaultRouter()
router.register('make-payment',TransactionViewSet, basename="make_payment")
router.register("get-balance",WalletViewSet,basename="get_wallet")
urlpatterns = [
    path('wallet/recharge/', WalletRechargeView.as_view(), name='wallet-recharge'),
    path('wallet/', WalletTransactionsView.as_view(), name="wallet-transactions"),
    
]+router.urls