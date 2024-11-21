from django.contrib import admin
from apps.restaurants.models import PickupLocation,MenuCategory,MenuItem,MenuImage

@admin.register(PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display=["id","street_address1","street_address2","city","postal_code"]
    fields = ["name","street_address1","street_address2","city","state","postal_code"]

 
@admin.register(MenuCategory)   
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]
    fields=["name"]
    
@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display=["id","name","price","category"]
    fields=["name","price","description","calories","protein","fats","carbs","category"]
 

    
@admin.register(MenuImage)
class MenuImagesAdmin(admin.ModelAdmin):
    list_display=["id","is_main","menu_item"]
    fields=["menu_item","image","is_main"]
   

    
    
    

