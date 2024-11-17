from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.restaurants.serializers import (
    RestaurantApiSerializer ,
    MenuCategorySerializer,
    ListMenuItemSerializer,
    CreateMenuItemSerializer,
    ListMenuImagesSerializer
)
from apps.restaurants.models import Restaurant,MenuCategory,MenuItem,MenuImage

class RestaurantApi(ModelViewSet):
    """ 
        Api for handling restaurants
    """
    http_method_names = ["get","post","delete"]
    serializer_class = RestaurantApiSerializer
    queryset = Restaurant.objects.all()
    
class MenuCategoryApi(ModelViewSet):
    """
        Api for handling Menu categories

    """
    http_method_names = ["get","post","delete"]
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all()
    
class MenuItemApi(ModelViewSet):
    """ 
        Api for handle Menu items 
        
    """
    http_method_names = ["get","post","delete"]
    serializer_class = ListMenuItemSerializer
    queryset = MenuItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListMenuItemSerializer
        return CreateMenuItemSerializer
    
class MenuImagesApi(ListAPIView):
    serializer_class =ListMenuImagesSerializer
    queryset = MenuImage.objects.all()
    
    

        
    