from django.urls import path
from rest_framework import routers
from apps.restaurants.views import (
    RestaurantApi,
    MenuCategoryApi,
    MenuItemApi,
    MenuImagesApi

)

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('pickup-location', RestaurantApi, basename="pickup_location")
router.register("menu-items", MenuItemApi , basename="menu_items")

urlpatterns = [
    path("create-menu-images/",MenuImagesApi.as_view(),name="create-menu_images"),
    path("menu-category/",MenuCategoryApi.as_view(),name="menu_category"),
 
]+router.urls+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)