from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile
from accounts.models import User

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

    snipped = serializers.ReadOnlyField(source="get_snipped")
    relative_url = serializers.URLField(
        source="get_absolute_api_url", read_only=True
    )
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "snipped",
            "relative_url",
            "absolute_url",
            "category",
            "status",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        reps = super().to_representation(instance)

        request = self.context.get("request")
        if request.parser_context.get("kwargs").get("pk"):
            reps.pop("absolute_url")
            reps.pop("relative_url")
            reps.pop("snipped")

            reps["state"] = "single"

        else:
            reps.pop("content")
            reps["state"] = "list"

        reps["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data

        return reps

    def create(self, validated_data):
        # request = self.context.get('request')
        # users = User.objects.filter(id = self.context.get('request').user.id )
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
