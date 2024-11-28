from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from apps.users.models import EmailToken , User,UserAddress,UserProfile,UserCardDetails,Wallet,ContactUs
from django.shortcuts import get_object_or_404

class RegisterApiSerializer(serializers.ModelSerializer):
    """ 
        Serializer for creating user instance
    """
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}, write_only=True,required=True
    )
    confirm_password = serializers.CharField(
        label=_("confirm_password"), style={"input_type": "password"}, write_only=True , required=True
    )
    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "mobile_number",
            "password",
            "confirm_password",
        )

        
    def validate(self, data):
        if not data['email'] and not data['mobile_number']:
            raise serializers.ValidationError("You must provide either an email or a mobile number.")
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data.get("full_name"),
            email =validated_data.get("email"),
            mobile_number = validated_data.get("mobile_number"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user
    
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token
    
    def _get_user_address(self,user):
        user_address = UserAddress.objects.filter(user=user,is_billing = True).first()
        return {
            "street_address1":user_address.street_address1,
            "street_address2":user_address.street_address2,
            "suburbs": user_address.suburbs,
            "name": user_address.name,
            "city":user_address.city,
            "postal_code":user_address.postal_code 
        } if user_address else None
    
    def _get_user_profile(self,user):
        profile = UserProfile.objects.filter(user=user).first()
        return {
                "data_of_birth": profile.date_of_birth,
                "user_image": profile.user_image,
            } if profile else None
    
    
    def validate(self, attrs):
        identifier = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(username=identifier,password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        refresh = self.get_token(user)
        data = {
            "refresh_token":str(refresh),
            "access_token":str(refresh.access_token),
            "user":{
                "id": user.id,
                "email": user.email,
                "profile": self._get_user_profile(user),
                "primary_address": self._get_user_address(user),
                "full_name": user.full_name,
            }
        }
        return data
        
class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        obj = User.objects.filter(email=email).exists()
        if not obj:
            raise ValidationError("Email Not Exists")
        return super().validate(attrs)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(
        label="New Password", style={"input_type": "password"}, write_only=True
    )
    confirm_password = serializers.CharField(
        label="Confirm Password", style={"input_type": "password"}, write_only=True
    )

    def validate(self, data):
        token = data.get("token")
        user =self.context['request'].user
        if not EmailToken.objects.filter(user=user, email_token=token).exists():
            raise serializers.ValidationError("Invalid or expired token.")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}, write_only=True
    )
    confirm_password = serializers.CharField(
        label=_("confirm_password"), style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password", "confirm_password"]

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is not correct")
        return value

    def validate(self, value):
        new_password = value.get("new_password")
        confirm_password = value.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords Not matching")
        return value
    
    
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ["id", "name", "street_address1", "street_address2", "city", "postal_code", "suburbs"]
        
    def validate(self, attrs):
        if not attrs['postal_code']:
            raise serializers.ValidationError("Postal Code Missing.")
        return super().validate(attrs)
    
    def create(self,attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return UserAddress.objects.create(**attrs)
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user_image', 'date_of_birth']
        
class UserCardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCardDetails
        fields = [
            'id', 'card_number', 'card_fullname', 'card_cvv', 
            'card_expiry', 'preferred_payment', 'user', 'is_active'
        ]
        extra_kwargs = {
            'card_cvv': {'write_only': True}, 
        }

class ListWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'unique_id']
        read_only_fields = ['unique_id']

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'expiry', 'unique_id']
        read_only_fields = ['unique_id']
        
        
class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
        
        
class UpdateUserinfoSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    mobile_number = serializers.CharField(required=False, allow_blank=True)
    user_image = serializers.ImageField(required=False, allow_null=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    primary_address = serializers.SerializerMethodField()
    billing_address = serializers.SerializerMethodField()
    
    class Meta:
        fields = ['id', 'email', 'profile', 'primary_address', 'full_name', 'billing_address']
        model = User

    def get_primary_address(self, obj):
        try:
            instance = UserAddress.objects.get(user=obj, is_primary=True)
            serializer = UserAddressSerializer(instance)
            return serializer.data
        except:
            return None
    
    def get_billing_address(self, obj):
        try:
            instance = UserAddress.objects.get(user=obj, is_billing=True)
            serializer = UserAddressSerializer(instance)
            return serializer.data
        except:
            return None
    
    def get_profile(self, obj):
        try:
            instance = UserProfile.objects.get(user=obj)
            return UserProfileSerializer(instance).data
        except:
            return None

