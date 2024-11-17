from django.urls import path
from rest_framework import routers
from apps.restaurants.views import (
    RestaurantApi,
    MenuCategoryApi,
    MenuItemApi,
    MenuImagesApi

)


router = routers.DefaultRouter()
router.register('restaurants', RestaurantApi, basename="restaurants")
router.register("menu-category", MenuCategoryApi , basename="menu_category")
router.register("menu-items", MenuItemApi , basename="menu_items")

urlpatterns = [
    path("menu-images/",MenuImagesApi.as_view(),name="menu_images")
 
]+router.urls