from django.contrib import admin
from apps.transactions.models import Transaction,WalletCoupon,OrderCoupon

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=["id","user","amount","transaction_id","operation_type"]
    fields=["user","amount","order_type","transaction_id","transaction_from","operation_type"]
    search_fields=['user']
    
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
  
