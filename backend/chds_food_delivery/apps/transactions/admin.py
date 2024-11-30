from django.contrib import admin
from apps.transactions.models import WalletCoupon,OrderCoupon,Wallet
    
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
  

 
@admin.register(Wallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display=["id","user","balance","created_at","is_active"]
    fields=["user","balance","is_active"]
    search_fields=["user__email"]
  
