from rest_framework import serializers

from app.models import Post, Comment


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at", "parent_comment"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at", "parent_comment"]

    def validate(self, data):
        post = data.get("post")
        parent_comment = data.get("parent_comment")
        if post and parent_comment:
            if post != parent_comment.post:
                raise serializers.ValidationError(
                    "This reply does not belong to the specified post."
                )
        return data


class CommentDetailSerializer(serializers.ModelSerializer):
    replies = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "post",
            "text",
            "created_at",
            "parent_comment",
            "replies",
        ]


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "user", "content", "created_at", "post_comments"]
        read_only_fields = ["user"]

    def get_post_comments(self, instance):
        comments = instance.post_comments.prefetch_related("replies").all()
        serializer = self.fields["post_comments"].to_representation(comments)
        return serializer
