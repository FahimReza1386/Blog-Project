from rest_framework import serializers
from ...models import Post , Category



# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)
#     status = serializers.CharField(max_length=200)



class PostSerializer(serializers.ModelSerializer):

    """
         Read Only Groups
    """
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)

    snipped = serializers.ReadOnlyField(source='get_snipped')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only = True)
    absolute_url = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ["id" , "author" , "title" , "content" ,'snipped','relative_url', 'absolute_url' ,  "category" , "status" , "created_date" , "published_date"]
        # read_only_fields = ['title','content']


    def get_absolute_url(self , obj):
        request = self.context.get('request')
        return request.build_absolute_uri()

class CategorySerializer(serializers.ModelSerializer):

    class Meta :
        model = Category
        fields = ['id' , 'name']