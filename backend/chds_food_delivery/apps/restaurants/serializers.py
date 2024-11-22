from rest_framework import serializers
from apps.restaurants.models import PickupLocation,MenuCategory,MenuImage,MenuItem


class RestaurantApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupLocation
        fields ="__all__"
        

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields ="__all__"

class ListMenuImagesSerializer(serializers.ModelSerializer):
    """     
        Serializer for list Menu image
    """
    class Meta:
        model = MenuImage
        fields = ["id", 'image', 'is_main']
            

class ListMenuItemSerializer(serializers.ModelSerializer):
    item_images = serializers.SerializerMethodField()
    class Meta:
        model = MenuItem
        fields = ["name","description","price","item_images"]
    
    def get_item_images(self,obj):
        images = obj.images.all()
        return ListMenuImagesSerializer(images,many=True).data
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        calories_payload = instance.get_caloric_breakdown()
        final_payload = {**data,**calories_payload}
        return final_payload

class CreateMenuItemSerializer(serializers.ModelSerializer):
    """     
        Serializer for for creating menu items
    """
    class Meta:
        model = MenuItem
        fields = "__all__"
        
class CreateMenuImagesSerializer(serializers.ModelSerializer):
    """     
        Serializer for create Menu image
    """
    class Meta:
        model = MenuImage
        fields = ['menu_item', 'image', 'is_main']
        
    def create(self, validated_data):
        if validated_data["is_main"]:
            MenuImage.objects.filter(menu_item=validated_data['menu_item']).update(is_main=False)
        super().create(validated_data)