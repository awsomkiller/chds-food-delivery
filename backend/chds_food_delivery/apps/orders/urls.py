from django.urls import path
from rest_framework import routers
from apps.orders.views import OrdersApi


router =routers.DefaultRouter()
router.register("user-orders",OrdersApi,basename="orders-api")
urlpatterns = [
    
]+router.urls
