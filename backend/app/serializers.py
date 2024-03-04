from rest_framework import serializers

from app.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    child_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at", "parent_comment", "child_comment"]

    def get_child_comment(self, obj):
        replies = Comment.objects.filter(parent_comment=obj).values_list('id', flat=True)
        return list(replies)

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
    child_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "post",
            "text",
            "created_at",
            "parent_comment",
            "child_comment",
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
