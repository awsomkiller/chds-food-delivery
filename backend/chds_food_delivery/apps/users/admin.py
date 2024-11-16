from django.contrib import admin
from apps.users.models import User,UserAddress,UserProfile,UserCardDetails,Wallet
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields =["email"]
    list_display =["id","email","created_at"]
   
    
@admin.register(UserAddress)
class UserAdmin(admin.ModelAdmin):
    fields=["user","street_address","city","state","country","postal_code","is_primary"] 
    list_display =["id","user","street_address","city","created_at","updated_at"]
   
    
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    fields=["user_image","date_of_birth","user"] 
    list_display =["id","user","date_of_birth"]
   
    
@admin.register(UserCardDetails)
class UserAdmin(admin.ModelAdmin):
    fields=["user","card_number","card_fullname","card_cvv","card_expiry","preferred_payment","is_active"] 
    list_display =["id","user","card_fullname"]
   
    
@admin.register(Wallet)
class UserAdmin(admin.ModelAdmin):
    fields=["user","balance","expiry"] 
    list_display =["id","user","expiry"]
   
    