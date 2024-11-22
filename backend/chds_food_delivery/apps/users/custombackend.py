from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


User =get_user_model()

class EmailorMobileBackend(ModelBackend):
    
    def authenticate(self, request, username = ..., password = ..., **kwargs):
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(mobile_number=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None