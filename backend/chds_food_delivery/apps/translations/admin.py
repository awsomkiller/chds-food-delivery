from django.contrib import admin
from apps.translations.models import LanguageCategory,Translation

@admin.register(LanguageCategory)
class LanguageCategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"feature_name","feature_code"]
    search_fields = ['feature_name']
    
    
@admin.register(Translation)
class LanguageCategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"language","label"]
    search_fields = ['language']