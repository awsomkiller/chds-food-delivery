from django.contrib import admin
from apps.transactions.models import WalletCoupon,OrderCoupon
    
@admin.register(WalletCoupon)
class WalletCouponAdmin(admin.ModelAdmin):
    list_display=["id","recharge_amount","name"]
    fields=["recharge_amount","recharge_value","name","code"]
    search_fields=["amount"]

 
@admin.register(OrderCoupon)
class OrderCouponAdmin(admin.ModelAdmin):
    list_display=["id","name","discount_type","discount_upto"]
    fields=["name","code","discount_type","discount_upto"]
    search_fields=["discount_type"]
  
