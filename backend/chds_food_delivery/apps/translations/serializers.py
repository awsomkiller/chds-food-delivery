from rest_framework import serializers
from apps.translations.models import LanguageCategory,Translation


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCategory
        fields = "__all__"
        
class TranslationSerializer(serializers.ModelSerializer):
    """
    Serializer to only serialize GET request
    """
    feature = FeaturesSerializer(many=True)
    class Meta:
        model = Translation
        fields = ['id', 'label', 'value', 'language', 'feature']
