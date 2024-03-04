from rest_framework import serializers

from app.models import Post, Comment, SubComment


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = ["comment", "user", "text", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    sub_comments = SubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ["user", "post", "text", "created_at", "sub_comments"]


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ["user", "content", "created_at", "post_comments"]
        read_only_fields = [
            "user",
        ]
