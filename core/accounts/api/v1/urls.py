from django.urls import path
from . import views



urlpatterns = [
    # Registration

    path('registration/' , views.RegistrationApiView.as_view() , name="Registration"),

    # Change Password
    
    # Reset Password
    
    # Login Token
    
    # Login jwt




]