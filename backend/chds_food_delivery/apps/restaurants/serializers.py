from rest_framework import serializers
from apps.restaurants.models import PickupLocation, MenuCategory, MenuImage, MenuItem, MenuPortionPriceList, Addons, MenuItemTags, WorkingDays, TimeSlots,DeliveryPoint


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

class ListAddonSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Addons
        fields = "__all__"

class ListMenuItemsTags(serializers.ModelSerializer):
    class Meta:
        model = MenuItemTags
        fields = "__all__"
            
class ListPortionSerializer(serializers.ModelSerializer):
    portion_name = serializers.CharField(source='portion_item.name')
    portion_weight = serializers.CharField(source='portion_item.weight')
    addons = serializers.SerializerMethodField()

    class Meta:
        model = MenuPortionPriceList
        fields = ["id", "portion_name", "portion_weight", "price", "addons","calories","protein","carbs",'fats']

    def get_addons(self, obj):
        addons = obj.portion_item.addons.all()
        return ListAddonSerialzier(addons, many=True).data
        
class ListMenuItemSerializer(serializers.ModelSerializer):
    item_images = serializers.SerializerMethodField()
    portion = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    class Meta:
        model = MenuItem
        fields = "__all__"
    
    def get_item_images(self,obj):
        images = obj.images.all()
        return ListMenuImagesSerializer(images,many=True).data
        
    def get_portion(self,obj):
        portions = obj.menu_items_prices.all()
        return ListPortionSerializer(portions,many=True).data
    
    def get_tags(self, obj):
        tags = obj.tags.all()
        return ListMenuItemsTags(tags, many=True).data
   
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


class TimeslotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlots
        fields = "__all__"

        
        
class DeliveryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = "__all__"