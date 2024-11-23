from django.core.management.base import BaseCommand
from typing import Any
import json
from apps.restaurants.models import MenuItem,MenuCategory,PortionSize

class Command(BaseCommand):
    help_text = "Command for Load Menu items"
    
    file_location = "apps/restaurants/files/data_meal.json"
    def handle(self, *args: Any, **options: Any):
        if not MenuCategory.objects.filter(name="daily meals").exists:
            category_instance = MenuCategory.objects.create(name="daily meals")
        else:
            category_instance = MenuCategory.objects.get(name="daily meals")
            
        with open(self.file_location,"r") as file:
            menu_items = json.load(file)
            for menu_item in menu_items:
                try:
                    portion_sizes = PortionSize.objects.create(name=menu_item["available_meal_size"][0],
                                                               weight = menu_item['available_meal_size'][1])
                    item_data = {
                        "name":menu_item['name'],
                        "price":menu_item['price'],
                        "description":menu_item['description'],
                        "calories":menu_item['calories'],
                        "protein":menu_item['protein'],
                        "fats":menu_item['fat'],
                        "carbs":menu_item['carbs'],
                        "category":category_instance,    
                        
                    }
                   
                    instance  = MenuItem.objects.create(**item_data)
                    instance.portion_sizes.add(portion_sizes)
                    
                    self.stdout.write(self.style.SUCCESS(f"{instance.name} menu item added"))
        
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{menu_item['name']} Failed to add menu item added"))