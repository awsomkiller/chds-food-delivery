from django.urls import path
from rest_framework import routers
from apps.users.views import (
    RegisterAPI,
    LoginApiView,
    ForgetApiView,
    ChangePasswordAPI,
    UserAddressesApi,
    UserProfileApi,
    UserCardDetailsViewSet,
    WalletViewSet,
    ResetPasswordAPI,
    ContactusApi,
    UpdateUserinfoApi,
    UserDetails,
    UpdatePrimaryAddressApi,
    RefreshTokenApiView
)


router = routers.DefaultRouter()
router.register('user-address', UserAddressesApi, basename="user_addresses")
router.register("user-profile", UserProfileApi , basename= "user_profile")
router.register("user-cards",UserCardDetailsViewSet , basename="user_card_details")
router.register('user-wallet', WalletViewSet, basename='user_wallet')

urlpatterns = [
    path("register-user/",RegisterAPI.as_view() , name="register_user"),
    path("login/",LoginApiView.as_view() , name="login"),
    path("refresh/", RefreshTokenApiView.as_view(), name="refresh-token"),
    path("details/", UserDetails.as_view(), name="user-details"),
    path("forget-password/",ForgetApiView.as_view(), name="forget_password"),
    path("reset-password/",ResetPasswordAPI.as_view(), name="forget_password"),
    path("change-password/",ChangePasswordAPI.as_view() , name ="change_password"),
    path("contactus/",ContactusApi.as_view(), name="contactus"),
    path("update-user-info/",UpdateUserinfoApi.as_view(),name="update_user_info"),
    path("update-primary-address/<int:pk>/",UpdatePrimaryAddressApi.as_view(),name="update-primary-address")
    # path("user-wallet/",UserWalletApi.as_view(),name="user_wallet")

]+router.urls