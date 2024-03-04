from rest_framework import viewsets

from app.models import Post
from app.serializers import (
    PostSerializer,
    PostListSerializer,
    PostDetailSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get_queryset(self):
        queryset = Post.objects.all()
        # filtering by content
        content = self.request.query_params.get("content")
        if content:
            queryset = queryset.filter(content__icontains=content)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer
