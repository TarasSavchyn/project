from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.content[:25]}"


class SubComment(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="sub_comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_sub_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SubComment by {self.user.username} on Comment {self.comment.text[:25]}"
