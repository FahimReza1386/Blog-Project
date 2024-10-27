from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView # type: ignore
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    # Registration

    path('registration/' , views.RegistrationApiView.as_view() , name="Registration"),

    # Change Password
    path('change-password/' , views.CustomChangePasswordApi.as_view() , name="Change-Password"),
    # Reset Password
    
    # Login Token
    path('token/login/' , views.CustomObtainAuthToken.as_view() , name="Token Login"),
    path('token/logout/' , views.CustomDiscardAuthToken.as_view() , name="Token Logout"),

    # Create and Refresh and Verify with jwt
    #     
    # path('jwt/create/' , TokenObtainPairView.as_view() , name="Create-JWT"),
    # path('jwt/refresh/' , TokenRefreshView.as_view() , name="Refresh-JWT"),
    # path('jwt/verify/' , TokenVerifyView.as_view() , name="Verify-JWT"),


    # Create and Refresh and Verify (Custom) with jwt
    path('jwt/create/' , views.CustomTokenObtainPairView.as_view() , name="Create-JWT"),
    path('jwt/refresh/' , views.CustomTokenRefreshView.as_view() , name="Refresh-JWT"),
    path('jwt/verify/' , views.CustomTokenVerifyView.as_view() , name="Verify-JWT"),

    # Profile
    path('profile/' , views.ProfileApiView.as_view() , name ="Profile")

]