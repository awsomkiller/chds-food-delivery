from django.contrib import admin
from apps.restaurants.models import Restaurant,MenuCategory,MenuItem,MenuImage

@admin.register(Restaurant)
class RestaurentAdmin(admin.ModelAdmin):
    list_display=["id","name","location","status","phone_number"]
    fields=["name","location","code","from_time","to_time","status","phone_number"]

 
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
    list_display=["id","is_main"]
    fields=["menu_item","image","is_main"]
   

    
    
    

