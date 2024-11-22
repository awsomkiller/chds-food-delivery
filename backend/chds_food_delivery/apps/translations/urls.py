from django.urls import path

from apps.translations import views

app_name = 'translation'

urlpatterns = [
    path('feature/', views.ListLanguageFeatureView.as_view({'get': 'list'}), name="languages-feature-list"),
    path('language/<str:lc>/feature/<str:fc>/', views.FetchTranslationBasedOnFeatureView.as_view({"get":'list'}), name="feature-translation"),
    path('all', views.TranslationApi.as_view({'get': 'list'}), name="fetch-translations")
]