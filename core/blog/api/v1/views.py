from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializer


@api_view(["GET","POST"])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializer(post , many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        """
            Saving a post normally
        """

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)

        """
            Saving a post in a simpler way
        """
    
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(["GET","PUT","DELETE"]) 
def post_detail(request, id):
    # try :
    #     obj = Post.objects.get(pk=id)
    #     serializer = PostSerializer(obj)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response('object does not exist' , status=404)
    obj = get_object_or_404(Post,pk=id , status=True)
    if request.method == "GET":
        serializer = PostSerializer(obj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(obj,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        obj.delete()
        return Response({'detail' : 'item removed successfully'})
