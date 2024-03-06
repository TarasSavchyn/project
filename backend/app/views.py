from urllib import request

from rest_framework import viewsets
from app.models import Comment
from app.serializers import (
    CommentSerializer,
)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        if self.action == "list":
            return Comment.objects.filter(parent_comment__isnull=True)
        return Comment.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
