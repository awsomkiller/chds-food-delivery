from django.urls import path
from rest_framework import routers
from apps.restaurants.views import (
    RestaurantApi,
    MenuCategoryApi,
    MenuItemApi,
    MenuImagesApi,
    TimeSlotsView,
    DeliveryPointApi
)

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('pickup-location', RestaurantApi, basename="pickup_location")
router.register("items", MenuItemApi , basename="menu_items")
router.register("delivery-point", DeliveryPointApi , basename="delivery_point")

urlpatterns = [
    path("images/",MenuImagesApi.as_view(),name="create-menu_images"),
    path("category/",MenuCategoryApi.as_view(),name="menu_category"),
    path("timeslots/", TimeSlotsView.as_view(), name="list-timeslots")
 
]+router.urls+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)