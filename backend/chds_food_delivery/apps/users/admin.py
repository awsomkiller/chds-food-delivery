from django.contrib import admin
from apps.users.models import User,UserAddress,UserProfile,UserCardDetails,Wallet,ContactUs
from django.contrib.auth.admin import UserAdmin



@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields =["email"]
    list_display =["id","email","created_at"]
    ordering = ['email']
   
    fieldsets = (
        (None, {'fields': ('email', 'password',"full_name","mobile_number")}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    fields=["user","street_address1","street_address2","suburbs","city","state","postal_code","is_primary","is_billing"] 
    list_display =["id","user","street_address1","street_address2","city","created_at","updated_at"]
   
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields=["user_image","date_of_birth","user"] 
    list_display =["id","user","date_of_birth"]
   
    
@admin.register(UserCardDetails)
class UserCardDetailsAdmin(admin.ModelAdmin):
    fields=["user","card_number","card_fullname","card_cvv","card_expiry","preferred_payment","is_active"] 
    list_display =["id","user","card_fullname"]
   
    
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    fields=["user","balance","expiry"] 
    list_display =["id","user","expiry"]
   
    
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display =["first_name","last_name","user",'email',"message","created_at"]
 

   
    