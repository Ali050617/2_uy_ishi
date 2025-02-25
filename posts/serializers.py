from django.utils.text import slugify
from rest_framework import serializers
from .models import Post
from category.serializers import CategorySerializer
from tags.serializers import TagSerializer
from author.serializers import AuthorSerializer


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = AuthorSerializer()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'comments_count']
        read_only_fields = ['slug']

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)