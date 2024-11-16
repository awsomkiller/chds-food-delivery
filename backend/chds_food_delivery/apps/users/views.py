from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.users.serializers import (
    RegisterApiSerializer,
    LoginSerializer,
    ForgetPasswordSerializer,
    VerifyPasswordSerializer
)
from django.shortcuts import get_object_or_404
import uuid

class RegisterAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterApiSerializer
    
    def post(self, request, *args,**kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if  serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
            return Response({"error": serializer.errors},status=status.HTTP_400_BAD_REQUEST,)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST,)
            
            
class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)            
    
class ForgetApiView(APIView):
    def post(self,request):
        serializer = ForgetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"].lower()

        token = uuid.uuid4()  
        # token_instance, _ = EmailToken.objects.update_or_create(
        #     user=request.user, defaults={"email_token": token}
        # )
        site_url = request.headers.get("Origin", "")
        # Sendresetpasswordlinkapi(site_url, email, token)

        return Response(
            {"message": "Password reset email sent successfully"},
            status=status.HTTP_200_OK,
        )
        
class VerifyResetPassword(APIView):
    serializer_class = VerifyPasswordSerializer
    permission_classes = ()

    def post(self, request, token, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]
        new_password = serializer.validated_data["password"]

        # token_instance = get_object_or_404(EmailToken, email_token=token)
        # user = token_instance.user

        # user.set_password(new_password)
        # user.save()
        # token_instance.delete()

        return Response(
            {"message": "Password updated successfully"}, status=status.HTTP_200_OK
        )

