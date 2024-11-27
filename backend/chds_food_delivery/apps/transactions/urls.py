from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.transactions.views import (
    TransactionViewSet,
    WalletRechargeView
)

router = DefaultRouter()
router.register('make-payment',TransactionViewSet, basename="make_payment")
urlpatterns = [
    path('wallet/recharge/', WalletRechargeView.as_view(), name='wallet-recharge'),
]+router.urls