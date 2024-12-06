from django.shortcuts import render
from apps.translations.models import Module,Translation
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet,ViewSet
from rest_framework.permissions import AllowAny
from apps.translations.serializers import TranslationSerializer,ModulesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ListLanguageFeatureView(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Module.objects.all()
    serializer_class = ModulesSerializer

class TranslationListApi(APIView):
    """
    API view to retrieve list of translations.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        module = request.query_params.get('module')
        translations = Translation.objects.all()

        if module:
            translations = translations.filter(module=module)

        serializer = TranslationSerializer(translations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
        