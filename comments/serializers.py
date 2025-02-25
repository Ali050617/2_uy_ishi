from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author_email = serializers.EmailField(validators=[serializers.EmailValidator()])

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']

    def get_replies(self, obj):
        if obj.parent_comment:
            return None
        replies = Comment.objects.filter(parent_comment=obj)
        return CommentSerializer(replies, many=True).data

    def validate_parent_comment(self, value):
        if value and value.parent_comment and value.parent_comment.parent_comment:
            raise serializers.ValidationError("Only 3 levels of nested comments are allowed.")
        return value