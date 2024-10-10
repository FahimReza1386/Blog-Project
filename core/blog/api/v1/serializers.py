from rest_framework import serializers
from ...models import Post



# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)
#     status = serializers.CharField(max_length=200)



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id" , "author" , "title" , "content" , "category" , "status" , "created_date" , "published_date"]