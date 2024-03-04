from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="child_comment"
    )

    def __str__(self):
        comment_type = "Reply" if self.parent_comment else "Comment"
        parent_type = "Comment" if self.parent_comment else "Post"
        content_preview = (
            self.parent_comment.text[:25]
            if self.parent_comment
            else self.post.content[:25]
        )

        return (
            f"{comment_type} by {self.user.username} on {parent_type} {content_preview}"
        )

    class Meta:
        ordering = ["created_at"]
