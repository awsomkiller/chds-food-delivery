from django.shortcuts import render
from apps.translations.models import Module,Translation
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet,ViewSet
from rest_framework.permissions import AllowAny
from apps.translations.serializers import TranslationSerializer,ModulesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class ListLanguageFeatureView(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Module.objects.all()
    serializer_class = ModulesSerializer

class TranslationApi(ModelViewSet):
    """
    A simple ViewSet for viewing languages.
    """
    permission_classes = [AllowAny]
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    ordering_fields = ['label', 'value', 'language']
    search_fields=["label", "value", "language"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        language_id = self.request.query_params.get('language')
        feature_id = self.request.query_params.get('feature')

        if language_id:
            queryset = queryset.filter(language__id=language_id)

        if feature_id:
            queryset = queryset.filter(feature__id=feature_id)

        return queryset
    
class FetchTranslationBasedOnFeatureView(ViewSet):
    """
    View to fetch translation for feature/ module for a single language.
    """
    permission_classes = [AllowAny]
    serializer_class = TranslationSerializer

 
    def fetch_feature_instance(self, fc):
        return get_object_or_404(Module, feature_code=fc)
    
    def fetch_translation_data(self, languageInstance, featureInstance):
        instances = Translation.objects.filter(language=languageInstance, feature=featureInstance.id)
        return self.serializer_class(instances, many=True).data

    def list(self, request, lc, fc):
        languageInstance = self.fetch_language_instance(lc)
        featureInstance = self.fetch_feature_instance(fc)

        try:
           return Response({
               "instances":self.fetch_translation_data(languageInstance, featureInstance)
           }, status=status.HTTP_200_OK)

        except Exception as exc:
            return Response({
                    "exception":str(exc).strip("\n"),
                }, status = status.HTTP_400_BAD_REQUEST)
        