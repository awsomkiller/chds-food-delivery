from django.contrib import admin
from apps.orders.models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id',"pickup_location","user","order_time","delivery_date","status","amount"]
    fields = ["pickup_location","user","order_time","delivery_time","status","amount","transaction","menu_item"]

