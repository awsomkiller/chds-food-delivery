from rest_framework import serializers
from apps.translations.models import Module,Translation


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        
class TranslationSerializer(serializers.ModelSerializer):
    """
    Serializer to only serialize GET request
    """
    module = ModulesSerializer()
    class Meta:
        model = Translation
        fields = ['id', 'label', 'value', 'language', 'module']
