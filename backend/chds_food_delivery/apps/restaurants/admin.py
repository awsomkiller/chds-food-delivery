from django.contrib import admin
from apps.restaurants.models import PickupLocation,MenuCategory,MenuItem,MenuImage,PortionSize,MenuPortionPriceList,Addons ,TimeSlots,WorkingDays, MenuItemTags,DeliveryPoint

@admin.register(PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display=["id","street_address1","street_address2","city","postal_code"]
    fields = ["name","street_address1","street_address2","city","state","postal_code", "is_active"]
    search_fields = ['city', 'postal_code', 'name']
 

@admin.register(MenuCategory)   
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]
    fields=["name"]
    search_fields=['name']
    

@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display=["id","name","is_popular","is_best_selling"]
    fields=["name","category", "tags","is_best_selling","is_popular", "trans_code", "trans_desc_code", "is_active"]
    search_fields = ['name','category__name']
    list_filter = ['category', "is_best_selling", "is_popular", "is_active"]
    

@admin.register(MenuImage)
class MenuImagesAdmin(admin.ModelAdmin):
    list_display=["id","is_main","menu_item"]
    fields=["menu_item","image","is_main"]
    search_fields = ['menu_item__name']
    list_filter = ['menu_item']    
  

@admin.register(PortionSize)
class PortionSizeAdmin(admin.ModelAdmin):
    list_display=["id", "code", "portion_weight", "name"]
    fields=["name", "weight", "code", "addons"]
    search_fields = ["name", "code", "addons"]

    def portion_weight(self, obj):
        return f"{obj.weight} g"
  

@admin.register(MenuPortionPriceList)
class PortionSizePriceAdmin(admin.ModelAdmin):
    list_display=["id","menu_item","portion_item","item_price","carbs","calories","fats","protein"]
    fields=["menu_item","portion_item","price","carbs","calories","fats","protein", "is_active"]
    search_fields = ['price',"menu_item__name","portion_item__name"]
    list_filter = ["menu_item", "portion_item"]
   
    def item_price(self, obj):
        return f"{obj.price}A$"
    

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
    
@admin.register(MenuItemTags)
class TagsAdmin(admin.ModelAdmin):
    list_display= ["id", "name"]
    fields = ["name"]
    
@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ['id',"name","price","postal_code"]
    fields = ["name","price","postal_code", "is_active"]
    search_fields = ['postal_code',"name"]