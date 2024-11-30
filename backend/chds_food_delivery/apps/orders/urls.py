from django.urls import path
from apps.orders.views import OrderCreateView, stripe_webhook,ListOrders


urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="Order-Create"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
    path("list-orders/",ListOrders.as_view(),name="list_orders")
]