from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.transactions.views import (
    TransactionViewSet,
    WalletRechargeView,
    WalletTransactionsView,WalletViewSet,
    OrderCouponViewSet,
    WalletCouponViewSet
    )

router = DefaultRouter()
router.register('make-payment',TransactionViewSet, basename="make_payment")
router.register("get-balance",WalletViewSet,basename="get_wallet")
router.register("coupons/orders", OrderCouponViewSet, basename="coupons-order")
router.register("coupons/wallet", WalletCouponViewSet, basename="coupone-wallet")
urlpatterns = [
    path('wallet/recharge/', WalletRechargeView.as_view(), name='wallet-recharge'),
    path('wallet/', WalletTransactionsView.as_view(), name="wallet-transactions"),
    
]+router.urls