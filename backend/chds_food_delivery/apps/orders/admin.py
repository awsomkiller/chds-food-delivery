from django.contrib import admin
from apps.orders.models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id',"restaurant_id","user","order_time","delivery_time","status","amount"]
    fields = ["restaurant_id","user","order_time","delivery_time","status","amount","transaction","menu_item"]

