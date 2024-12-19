from django.contrib import admin
from apps.translations.models import Translation , Module

@admin.register(Module)
class LanguageCategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"feature_name","feature_code"]
    search_fields = ['feature_name']
    
    
@admin.register(Translation)
class LanguageCategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"language","label", "value"]
    search_fields = ['language', 'label', 'value']
    list_filter = ['module', 'language']