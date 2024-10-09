from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    # path('test', views.indexview.as_view(), name='index Page1'),
    # path('test-mktbk', RedirectView.as_view(pattern_name='blog:index Page1'), name='index Page'),
    path('rdcmktb/<int:pk>', views.redirectToMaktab.as_view(), name='index Page'),
    path('post', views.Posts.as_view(), name='Post Page'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post-detail'),
    path('post/', views.Posts.as_view(), name='post-detail2'),
    path('post/create', views.PostCreateView.as_view(), name='PostCreateView'),
    path('post/<int:pk>/update/', views.UpdatePost.as_view(), name='UpdatePost'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='DeletePost'),
    path('api/v1/' , include('blog.api.v1.urls')),

]