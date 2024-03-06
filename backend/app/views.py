from rest_framework import viewsets
from app.models import Comment
from app.serializers import CommentSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.filter(parent_comment__isnull=True)

        sort_options = {
            'username': 'user__username',
            '-username': '-user__username',
            'user_email': 'user__email',
            '-user_email': '-user__email',
            'created_at': 'created_at',
            '-created_at': '-created_at',
        }

        sort_by = self.request.query_params.get('sort_by')
        if sort_by in sort_options:
            queryset = queryset.order_by(sort_options[sort_by])

        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="sort_by",
                type={"type": "string"},
                description="Filter all top-level comments.",
                required=False,
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
