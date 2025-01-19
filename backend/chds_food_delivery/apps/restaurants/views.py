from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView
from apps.restaurants.serializers import (
    RestaurantApiSerializer ,
    MenuCategorySerializer,
    ListMenuItemSerializer,
    CreateMenuItemSerializer,
    CreateMenuImagesSerializer,
    ListAddonSerialzier,
    DeliveryPointSerializer,
    TimeslotsSerializer
)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.restaurants.models import PickupLocation,MenuCategory,MenuItem,MenuImage,Addons, TimeSlots,DeliveryPoint
from rest_framework.permissions import AllowAny


class RestaurantApi(ModelViewSet):
    """ 
        Api for handling restaurants
    """
    http_method_names = ["get"]
    serializer_class = RestaurantApiSerializer
    queryset = PickupLocation.objects.filter(is_active=True)
    permission_class = []
    
class MenuItemApi(ModelViewSet):
    """ 
        Api for handle Menu items   
    """
    http_method_names = ["get","post","delete"]
    serializer_class = ListMenuItemSerializer
    queryset = MenuItem.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name',"category__name"]
    permission_classes = [AllowAny,]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ListMenuItemSerializer
        return CreateMenuItemSerializer

class MenuCategoryApi(ListAPIView):
    """     
        API for listing categories
    """
    permission_classes = [AllowAny]
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
      
class MenuAddonApi(ListAPIView):
    """     
        API for listing categories
    """
    serializer_class = ListAddonSerialzier
    queryset = Addons.objects.all()


class TimeSlotsView(APIView):

    serializer_class = TimeslotsSerializer
    permission_classes = [AllowAny]
    
    def get(self, request):
        instances = TimeSlots.objects.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeliveryPointApi(ReadOnlyModelViewSet):
    serializer_class=DeliveryPointSerializer
    queryset=DeliveryPoint.objects.filter(is_active=True)