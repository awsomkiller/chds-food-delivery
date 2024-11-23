from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.transactions.views import (
    TransactionViewSet
)

router = DefaultRouter()
router.register('make-payment',TransactionViewSet, basename="make_payment")
urlpatterns = []+router.urls