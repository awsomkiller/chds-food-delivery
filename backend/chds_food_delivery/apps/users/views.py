import base64
import imghdr
import uuid
from django.core.files.base import ContentFile
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
    UserAddressSerializer,
    UserProfileSerializer,
    UserCardDetailsSerializer,
    WalletSerializer,
    ListWalletSerializer,
    ContactusSerializer,
    UpdateUserinfoSerializer,
    UserDetailsSerializer,
    UpdatePrimaryUserAddressSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from apps.users.models import User , EmailToken ,UserAddress,UserCardDetails,UserProfile,Wallet,ContactUs
from django.utils.crypto import get_random_string
from apps.users.email import Sendresetpasswordlinkapi
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class RegisterAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterApiSerializer
    
    def post(self, request, *args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({"errors": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"errors": {"general": "An unexpected error occurred."}}, status=status.HTTP_400_BAD_REQUEST)
            
            
class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,) 
    

class RefreshTokenApiView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        refresh_token_str = request.data.get('refresh_token')

        if not refresh_token_str:
            return Response(
                {'error': 'Refresh token not provided.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            refresh_token = RefreshToken(refresh_token_str)
            user = User.objects.get(id=refresh_token['user_id']) 

            if refresh_token['exp'] < timezone.now().timestamp():
                raise InvalidToken('Refresh token has expired.')

            new_refresh_token = RefreshToken.for_user(user)
            new_access_token = new_refresh_token.access_token
        
            return Response(
                {
                    'access_token': str(new_access_token),
                    'refresh_token': str(new_refresh_token)
                },
                status=status.HTTP_200_OK
            )

        except TokenError as e:
            return Response(
                {'error': 'Invalid or expired refresh token.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except InvalidToken as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            return Response(
                {'error': 'An error occurred while refreshing the token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        


class UserDetails(APIView):
    def get(self, request):
        serializer = UserDetailsSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        full_name = request.data.get('full_name')
        profile_picture = request.data.get('profile_picture')  # Base64 string

        # Update full name if provided
        if full_name:
            user.full_name = full_name
            user.save()

        # Process profile picture if provided
        if profile_picture:
            # Validate and decode base64 string
            try:
                # Remove the header if present (e.g., "data:image/png;base64,")
                if ',' in profile_picture:
                    header, profile_picture = profile_picture.split(',', 1)
                
                # Decode the base64 string
                decoded_file = base64.b64decode(profile_picture)
            except (TypeError, ValueError) as e:
                return Response(
                    {"error": "Invalid image data."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Determine the image type
            image_type = imghdr.what(None, decoded_file)
            if image_type not in ['jpeg', 'png', 'gif']:
                return Response(
                    {"error": "Unsupported image type."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Generate a unique file name
            file_extension = 'jpg' if image_type == 'jpeg' else image_type
            file_name = f"{uuid.uuid4()}.{file_extension}"
            
            # Create a ContentFile
            image_file = ContentFile(decoded_file, name=file_name)
            
            # Get or create the UserProfile
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            
            # Assign the image to the user_profile's ImageField
            user_profile.user_image = image_file
            user_profile.save()

        return Response({"message": "Profile updated successfully."}, status=status.HTTP_200_OK)         
    
class ForgetApiView(APIView):
    def post(self,request):
        try:
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
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

        
class ResetPasswordAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ResetPasswordSerializer(data=request.data, context={"request":request})
            if serializer.is_valid(raise_exception=True):
                email = serializer.validated_data["email"]
                new_password = serializer.validated_data["new_password"]
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPI(APIView):
    serializer_class = ChangePasswordSerializer
    
    def post(self, request):
        try:
            instance = self.request.user
            serializer = self.serializer_class(
                data=request.data, context={"request": request}
            )
            if serializer.is_valid(raise_exception=True):
                instance.set_password(serializer.validated_data.get("new_password"))
                instance.save()
                return Response({"message":"Password Changes Successfully"},status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)



class UserAddressesApi(ModelViewSet):
    """ 
        API for Managing User Address
    """
    http_method_names=['get',"post","delete"]
    serializer_class = UserAddressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
    
class UserProfileApi(ModelViewSet):
    """
    API endpoint for managing user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) 


class UserCardDetailsViewSet(ModelViewSet):
    """
    API endpoint for managing user card details.
    """
    queryset = UserCardDetails.objects.all()
    serializer_class = UserCardDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) 



class WalletViewSet(ModelViewSet):
    """
    API endpoint for managing wallets.
    """
    http_method_names=['get',"post","options"]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action=="list":
            return ListWalletSerializer
        return self.serializer_class
            

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        

class ContactusApi(generics.CreateAPIView):
    serializer_class = ContactusSerializer
    queryset = ContactUs.objects.all()
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer,request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self,serializer ,request):
        if request.user.is_authenticated:
            serializer.save(user =self.request.user)
        else:
            serializer.save()
    
class UpdateUserinfoApi(APIView):
    serializer_class = UpdateUserinfoSerializer
    
    def update_user_profile(self,user_image,date_of_birth):
        user_profile,_ = UserProfile.objects.get_or_create(user=self.request.user)
        update_fields = {}
        if date_of_birth:
            update_fields["date_of_birth"] = date_of_birth
        if user_image:
            update_fields["user_image"] = user_image

        if update_fields:
            for field, value in update_fields.items():
                setattr(user_profile, field, value)
            user_profile.save(update_fields=update_fields.keys())
            
            
    def update_user_info(self,full_name,email,mobile_number):
        user = self.request.user
        update_fields = {}
        if full_name:
            update_fields["full_name"] = full_name
        if email:
            update_fields["email"] = email
        if mobile_number:
            update_fields["mobile_number"] = mobile_number

        if update_fields:
            for field, value in update_fields.items():
                setattr(user, field, value)
            user.save(update_fields=update_fields.keys())
    
    def post(self,request,*args,**kwargs):
        try:
            serializer = self.serializer_class(data= request.data)
            serializer.is_valid(raise_exception=True)
            full_name = serializer.validated_data.get('full_name')
            email = serializer.validated_data.get("email")
            mobile_number = serializer.validated_data.get("mobile_number")
            user_image =  serializer.validated_data.get("user_image")
            date_of_birth = serializer.validated_data.get("date_of_birth")
            self.update_user_profile(user_image,date_of_birth)
            self.update_user_info(full_name,email,mobile_number)
            return Response({"message":"Updated Successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
            
        
        
        
        
class UpdatePrimaryAddressApi(generics.UpdateAPIView):
    serializer_class = UpdatePrimaryUserAddressSerializer
    queryset = UserAddress.objects.all()
    
    
    def update(self, request,pk, *args, **kwargs):
        user_address_instance = self.get_object()
        if user_address_instance.user != request.user:
            raise ValidationError("You are not authorised to Update the primary address.")
        return super().update(request, *args, **kwargs)
    