from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns = [
    # Registration

    path('registration/' , views.RegistrationApiView.as_view() , name="Registration"),
    path('token/login/' , ObtainAuthToken.as_view() , name="Token Login"),

    # Change Password
    
    # Reset Password
    
    # Login Token
    
    # Login jwt




]