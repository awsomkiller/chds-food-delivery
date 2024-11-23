from django.contrib import admin
from apps.restaurants.models import PickupLocation,MenuCategory,MenuItem,MenuImage,PortionSize,MenuPortionPriceList,Addons ,TimeSlots,WorkingDays
@admin.register(PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display=["id","street_address1","street_address2","city","postal_code"]
    fields = ["name","street_address1","street_address2","city","state","postal_code"]
    search_fields = ['city']
 
@admin.register(MenuCategory)   
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]
    fields=["name"]
    search_fields=['name']
    
@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display=["id","name","price","category"]
    fields=["name","price","description","calories","protein","fats","carbs","category","portion_sizes"]
    search_fields = ['name','price','category__name']
 

    
@admin.register(MenuImage)
class MenuImagesAdmin(admin.ModelAdmin):
    list_display=["id","is_main","menu_item"]
    fields=["menu_item","image","is_main"]
    search_fields = ['is_main']
   

    
  
@admin.register(PortionSize)
class PortionSizeAdmin(admin.ModelAdmin):
    list_display=["id","name","weight"]
    fields=["name","weight"]
    search_fields = ['name']
    
   
    
  
@admin.register(MenuPortionPriceList)
class PortionSizePriceAdmin(admin.ModelAdmin):
    list_display=["id","menu_item","portion_item","formatted_price"]
    fields=["menu_item","portion_item","price"]
    search_fields = ['price',"menu_item__name","portion_item__name"]
   
    def formatted_price(self, obj):
        return f"{obj.price}$"

    
@admin.register(Addons)
class AddonsAdmin(admin.ModelAdmin):
    list_display=["id","name","price"]
    fields=["name","price"]
    search_fields =['name','price']
    
   
    
@admin.register(TimeSlots)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display=["id","name","type"]
    fields=["name","type"]
    search_fields =['name','type']
    
    
    
@admin.register(WorkingDays)
class WorkingDaysAdmin(admin.ModelAdmin):
    list_display=["id","date","is_active"]
    fields=["date","time_slot","is_active"]
    search_fields =['date','is_active']
    
    

