from django.urls import path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns = [
    # Registration

    path('registration/' , views.RegistrationApiView.as_view() , name="Registration"),

    # Change Password
    
    # Reset Password
    
    # Login Token
        path('token/login/' , views.CustomObtainAuthToken.as_view() , name="Token Login"),
        path('token/logout' , views.CustomDiscardAuthToken.as_view() , name="Token Logout")
    
    # Login jwt




]