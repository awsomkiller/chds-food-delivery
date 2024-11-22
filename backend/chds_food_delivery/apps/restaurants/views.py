from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from apps.restaurants.serializers import (
    RestaurantApiSerializer ,
    MenuCategorySerializer,
    ListMenuItemSerializer,
    CreateMenuItemSerializer,
    CreateMenuImagesSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.restaurants.models import PickupLocation,MenuCategory,MenuItem,MenuImage

class RestaurantApi(ModelViewSet):
    """ 
        Api for handling restaurants
    """
    http_method_names = ["get","post","delete"]
    serializer_class = RestaurantApiSerializer
    queryset = PickupLocation.objects.all()
    
class MenuItemApi(ModelViewSet):
    """ 
        Api for handle Menu items   
    """
    http_method_names = ["get","post","delete"]
    serializer_class = ListMenuItemSerializer
    queryset = MenuItem.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name',"category__name"]

  
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListMenuItemSerializer
        return CreateMenuItemSerializer

class MenuCategoryApi(ListAPIView):
    """     
        API for listing categories
    """
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all()


class MenuImagesApi(ListCreateAPIView):
    """
        API for creating Create Menu images for menu items
    """
    serializer_class =CreateMenuImagesSerializer
    queryset = MenuImage.objects.all()
    
    def get_queryset(self):
        """
        Custom filtering logic based on 'menu_name' query parameter in the URL.
        """
        queryset = super().get_queryset()
        menu_name = self.request.query_params.get('menu_item')  # Custom parameter
        if menu_name:
            return queryset.filter(menu_item__name__icontains=menu_name)
        return queryset
    
    

        
    