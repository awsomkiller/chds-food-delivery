from django.contrib import admin
from apps.transactions.models import WalletCoupon,OrderCoupon,Wallet
    
@admin.register(WalletCoupon)
class WalletCouponAdmin(admin.ModelAdmin):
    list_display=["id","recharge_amount","name"]
    fields=["recharge_amount","recharge_value","name","code"]
    search_fields=["amount"]

 
@admin.register(OrderCoupon)
class OrderCouponAdmin(admin.ModelAdmin):
    list_display=["id","name", "name_code", "desc_code", "discount_type","discount"]
    fields=["name", "code", "discount_type", "discount_upto", "is_active"]
    search_fields=["discount_type", "name", "name_code", "desc_code"]
    list_filter=["discount_type",]
    
    def discount(self, obj):
        if obj.discount_type == "FIXED_ITEM":
            return f"A$ {obj.discount_upto} per Item"
        elif obj.discount_type == "FIXED_ORDER":
            return f"A$ {obj.discount_upto} per Order"
        else:
            return f"{obj.discount_upto} % per Order"
    
 
@admin.register(Wallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display=["id","user","balance","created_at","is_active"]
    fields=["user","balance","is_active"]
    search_fields=["user__email"]
  
