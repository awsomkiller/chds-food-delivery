from rest_framework import serializers
from apps.restaurants.models import Restaurant,MenuCategory,MenuImage,MenuItem


class RestaurantApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields ="__all__"
        

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields ="__all__"
        
class ListMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["name","description","price"]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        calories_payload = instance.get_caloric_breakdown()
        final_payload = {**data,**calories_payload}
        return final_payload

class CreateMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        
class ListMenuImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuImage
        fields = ['id', 'menu_item', 'image', 'is_main']