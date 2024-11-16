from django.urls import path
from apps.users.views import (
    RegisterAPI,
    LoginApiView
)

urlpatterns = [
    path("register-user/",RegisterAPI.as_view() , name="register_user"),
    path("login/",LoginApiView.as_view() , name="login"),
    path("forget-password/",ForgetApiView.as_view(), name="api-forget_password"),

]