from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    # Registration

    path('registration/' , views.RegistrationApiView.as_view() , name="Registration"),

    # Change Password
    
    # Reset Password
    
    # Login Token
    path('token/login/' , views.CustomObtainAuthToken.as_view() , name="Token Login"),
    path('token/logout/' , views.CustomDiscardAuthToken.as_view() , name="Token Logout"),

    # Login jwt
    path('jwt/create/' , TokenObtainPairView.as_view() , name="Create-JWT"),
    path('jwt/refresh/' , TokenRefreshView.as_view() , name="Refresh-JWT"),
    path('jwt/verify/' , TokenVerifyView.as_view() , name="Verify-JWT"),


]