from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from apps.users.models import EmailToken , User,UserAddress


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
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        # if data["mobile_number"]
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

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(email=email,password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return super().validate(attrs)
        
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
        fields = ["street_address","city","state","country","postal_code","is_primary"]
        
    def validate(self, attrs):
        if not attrs['postal_code']:
            raise serializers.ValidationError("Postal Code Missing.")
        return super().validate(attrs)
    
    def create(self,attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return UserAddress.objects.create(**attrs)