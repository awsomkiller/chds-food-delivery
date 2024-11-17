from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.users.serializers import (
    RegisterApiSerializer,
    LoginSerializer,
    ForgetPasswordSerializer,
    ResetPasswordSerializer,
    ChangePasswordSerializer,
    UserAddressSerializer
)
from django.shortcuts import get_object_or_404
import uuid
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from apps.users.models import User , EmailToken ,UserAddress
from django.utils.crypto import get_random_string
from apps.users.email import Sendresetpasswordlinkapi

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
        email = serializer.validated_data["email"]
        token =get_random_string(length=32) 
        EmailToken.objects.update_or_create(
            user=request.user,
            defaults={"email_token": token},
        )
        site_url = request.headers.get("Origin", "")
        Sendresetpasswordlinkapi(site_url, email, token)
        return Response(
            {"message": "Password reset email sent successfully"},
            status=status.HTTP_200_OK,
        )
        
class ResetPasswordAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data, context={"request":request})
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            new_password = serializer.validated_data["new_password"]
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPI(APIView):
    serializer_class = ChangePasswordSerializer
    
    def create(self, request):
        instance = self.request.user
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            instance.set_password(serializer.validated_data.get("new_password"))
            instance.save()
            return Response({"message":"Password Changes Successfully"},status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserAddressesApi(ModelViewSet):
    """ 
        API for Managing User Address
    """
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    
    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
    
class UserProfileApi(ModelViewSet):
    
    pass

class UserCardDetailsApi(ModelViewSet):
    pass


class UserWalletApi(generics.ListCreateAPIView):
    pass