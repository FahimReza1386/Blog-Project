from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ...models import Post
from .serializers import PostSerializer

"""
    Function Base View Api
"""



# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def post_list(request):
#     if request.method == "GET":
#         post = Post.objects.all()
#         serializer = PostSerializer(post , many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         """
#             Saving a post normally
#         """

#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # else:
#         #     return Response(serializer.errors)

#         """
#             Saving a post in a simpler way
#         """
    
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(["GET","PUT","DELETE"]) 
# @permission_classes([IsAuthenticated])
# def post_detail(request, id):
#     # try :
#     #     obj = Post.objects.get(pk=id)
#     #     serializer = PostSerializer(obj)
#     #     return Response(serializer.data)
#     # except Post.DoesNotExist:
#     #     return Response('object does not exist' , status=404)
#     obj = get_object_or_404(Post,pk=id , status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(obj)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(obj,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         obj.delete()
#         return Response({'detail' : 'item removed successfully'})


"""
Class Base View Api
"""

class PostList(APIView):
    
    """
        Getting a list of Post Model an Creating New Posts
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self , request):
        post = Post.objects.all()
        serializer = PostSerializer(post , many=True)
        return Response(serializer.data)

    def post(self , request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class PostDetail(APIView):
    """
        Getting and Putting and Deleting of the Post Model With Class Base View
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


    def get(self , request , id):
        post = get_object_or_404(Post,pk=id)
        serializer  = self.serializer_class(post)
        return Response(serializer.data)

    def put(self , request , id):
        post = get_object_or_404(Post,pk=id)
        serializer=self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self , request , id):
        post = get_object_or_404(Post , pk=id)
        post.delete()
        return Response({'detail' : 'item removed successfully .'})