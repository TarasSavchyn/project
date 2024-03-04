from rest_framework import serializers

from app.models import Post, Comment, SubComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = "__all__"
