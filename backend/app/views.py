from rest_framework import viewsets

from app.models import Post, Comment, SubComment
from app.serializers import (
    PostSerializer,
    CommentSerializer,
    SubCommentSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class SubCommentViewSet(viewsets.ModelViewSet):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

