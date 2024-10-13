from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'


router = DefaultRouter()
router.register('post' , views.PostModelViewSet , basename='post'),
router.register('category' , views.CategoryModelViewSet , basename='category'),

urlpatterns = router.urls

# urlpatterns = [
#     # path('', views.post_list, name='post_list'),
#     # path('post/<int:id>/', views.post_detail, name='post_list'),
#     # path('', views.PostList.as_view(), name='post_list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
#     path('post/' , views.PostViewSet.as_view({'get':'list','post':'create'}) , name='Post_View_Sets'),
#     path('post/<int:pk>/' , views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}) , name='Post_View_Set'),
# ]