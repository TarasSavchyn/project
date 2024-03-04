from rest_framework import serializers

from app.models import Post, Comment, SubComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'content', 'created_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'text', 'created_at']

class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = ['comment', 'user', 'text', 'created_at']

