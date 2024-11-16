from rest_framework import serializers
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

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
    email = serializers.EmailField(_("User Email"),required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        obj = User.objects.filter(email=email).exists()
        if not obj:
            raise ValidationError("Email Not Exists")
        return super().validate(attrs)

class VerifyPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        label=_("confirm_password"), style={"input_type": "password"}
    )
    token = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise ValidationError({"confirm_password": "Passwords do not match"})
        return attrs

    # def validate_token(self, value):
    #     if not EmailToken.objects.filter(email_token=value).exists():
    #         raise serializers.ValidationError("Invalid Token")
    #     return value
