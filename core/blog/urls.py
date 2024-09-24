from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path('test', views.indexview.as_view(), name='index Page1'),
    path('test-mktbk', RedirectView.as_view(pattern_name='blog:index Page1'), name='index Page'),
    path('rdcmktb/<int:pk>', views.redirectToMaktab.as_view(), name='index Page'),
]