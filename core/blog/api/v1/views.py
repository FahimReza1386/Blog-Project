from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListAPIView , ListCreateAPIView , CreateAPIView , RetrieveAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from ...models import Post , Category
from .serializers import PostSerializer , CategorySerializer
from rest_framework import mixins
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter
from .paginations import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend



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
'''
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
'''


'''
class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    """
        Getting a list of Post Model an Creating New Posts
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)
    
    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)


'''


# class PostList(ListCreateAPIView):
#     """
#         Getting a list of Post Model an Creating New Posts
#     """

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

'''
class PostDetail(APIView):
    """
        Getting and Putting and Deleting of the Post Model With Class Base View
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


    def get(self , request , pk):
        post = get_object_or_404(Post,pk=pk)
        serializer  = self.serializer_class(post)
        return Response(serializer.data)

    def put(self , request , pk):
        post = get_object_or_404(Post,pk=pk)
        serializer=self.serializer_class(post,data=request.data)
        serializer.is_valpk(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self , request , pk):
        post = get_object_or_404(Post , pk=pk)
        post.delete()
        return Response({'detail' : 'item removed successfully .'})
'''


'''
class PostDetail(GenericAPIView , mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin):
    """
        Getting and Putting and Deleting of the Post Model With Class Base View
    """


    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self , request , *args , **kwargs):
        return self.retrieve(request , *args , **kwargs)

    # def get(self , request , id):
    #     post = get_object_or_404(Post,pk=id)
    #     serializer  = self.serializer_class(post)
    #     return Response(serializer.data)
        

    def put(self , request , *args , **kwargs):
        return self.update(request , *args , **kwargs)

    # def put(self , request , id):
    #     post = get_object_or_404(Post,pk=id)
    #     serializer=self.serializer_class(post,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    def delete(self , request , *args , **kwargs):
        return self.destroy(request , *args , **kwargs)

    # def delete(self , request , id):
    #     post = get_object_or_404(Post , pk=id)
    #     post.delete()
    #     return Response({'detail' : 'item removed successfully .'})
'''


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """
#         Getting and Putting and Deleting of the Post Model With Class Base View
#     """


#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()



"""
    View Set Class Base View
"""


# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


#     def list(self , request):
#         serializer = self.serializer_class(self.queryset,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self , request , pk=None):
#         obj_post = get_object_or_404(self.queryset , pk=pk)
#         serializer = self.serializer_class(obj_post)
#         return Response(serializer.data)
    
#     def create(self , request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def update(self , request , pk=None):
#         obj=get_object_or_404(self.queryset , pk=pk)
#         serializer = self.serializer_class(obj,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def partial_update(self , request , pk=None):
#         obj = get_object_or_404(self.queryset , pk=pk)
#         serializer= self.serializer_class(obj , data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)

#     def destroy(self , request , pk=None):
#         obj_post = get_object_or_404(self.queryset , pk=pk)
#         obj_post.delete()
#         return Response({'detail' : 'item removed successfully'})



"""
    Model View Set in Class Base View
"""
class PostModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_fields = {'category':['exact','in'] , 'author':['exact'] , 'status':['exact']}
    search_fields = ['title','content']
    ordering_fields= ['category']
    # pagination_class = DefaultPagination



    @action(methods=['get'],detail=False)
    def get_ok(self , request):
        return Response({'detail':'ok'})

class CategoryModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()