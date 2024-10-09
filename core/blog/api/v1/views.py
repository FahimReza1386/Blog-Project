from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializer


@api_view()
def post_list(request):
    return Response({'name' : 'fahim'})


@api_view()
def post_detail(request, id):
    obj = Post.objects.get(pk=id)
    serializer = PostSerializer(obj)
    return Response(serializer.data)
