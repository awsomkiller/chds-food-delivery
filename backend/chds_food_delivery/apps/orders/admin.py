from django.contrib import admin
from apps.orders.models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id',"pickup_location","user","order_time","status","amount"]
    fields = ["pickup_location","user","order_time","order_type","delivery_location","status","amount","transaction","menu_item"]
    readonly_fields=['order_time']
    search_fields =['transaction__transaction_id','pickup_location__name', 'user__mobile_number', 'user__email']
    list_filter = ['pickup_location__name', "status"]
