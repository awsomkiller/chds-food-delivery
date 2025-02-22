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
    portion_code = serializers.CharField(source='portion_item.code')
    addons = serializers.SerializerMethodField()

    class Meta:
        model = MenuPortionPriceList
        fields = ["id", "portion_name", "portion_weight", "price", "addons","calories","protein","carbs",'fats', 'portion_code']

    def get_addons(self, obj):
        addons = obj.portion_item.addons.all()
        return ListAddonSerialzier(addons, many=True).data
        
class ListMenuItemSerializer(serializers.ModelSerializer):
    item_images = serializers.SerializerMethodField()
    portion = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    protein = serializers.SerializerMethodField()
    calories = serializers.SerializerMethodField()
    fats = serializers.SerializerMethodField()
    carbs = serializers.SerializerMethodField()

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
    
    def get_price(self, obj):
        instances = MenuPortionPriceList.objects.filter(menu_item=obj)
        prices = [int(instance.price) for instance in instances]
        min_price = min(prices) if prices else 0
        max_price = max(prices) if prices else 0
        return f"A${min_price} - A${max_price}"
    
    def fetch_menu_item(self, obj):
        instances = MenuPortionPriceList.objects.filter(menu_item=obj).exclude(portion_item__name='meal_set')
        return instances[0] if instances else None

    def get_protein(self, obj):
        instance = self.fetch_menu_item(obj)
        return instance.protein if instance else 0
    
    def get_fats(self, obj):
        instance = self.fetch_menu_item(obj)
        return instance.fats if instance else 0
    
    def get_carbs(self, obj):
        instance = self.fetch_menu_item(obj)
        return instance.carbs if instance else 0
    
    def get_calories(self, obj):
        instance = self.fetch_menu_item(obj)
        return instance.calories if instance else 0
   
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