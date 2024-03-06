from rest_framework import serializers
from rest_framework_recaptcha.fields import ReCaptchaField

from app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)
    child_comment = serializers.SerializerMethodField()
    recaptcha = ReCaptchaField(required=False)  # False only in dev

    class Meta:
        model = Comment
        fields = [
            "id",
            "username",
            "user_email",
            "text",
            "created_at",
            "parent_comment",
            "child_comment",
            "recaptcha",

        ]

    def get_child_comment(self, obj):
        children = Comment.objects.filter(parent_comment=obj)
        serializer = CommentSerializer(instance=children, many=True)
        return serializer.data
