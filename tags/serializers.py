from django.utils.text import slugify
from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'post_count']
        read_only_fields = ['slug']

    def get_post_count(self, obj):
        return obj.post_set.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)