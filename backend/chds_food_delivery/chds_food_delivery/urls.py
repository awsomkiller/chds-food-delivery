from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.users.urls")),
    path("api/translations/", include("apps.translations.urls")),
    path("api/transactions/", include("apps.transactions.urls")),
    path("api/items/", include("apps.restaurants.urls")),
    path("api/orders/",include("apps.orders.urls")),
    path("api-auth/", include("rest_framework.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
