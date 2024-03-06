import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


def post_photo_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.content[:8])}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/posts", filename)


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_comment",
    )

    photo = models.ImageField(
        upload_to=post_photo_file_path,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["created_at"]
