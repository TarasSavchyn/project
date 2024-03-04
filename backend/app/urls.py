from rest_framework.routers import DefaultRouter
from app.views import PostViewSet, CommentViewSet, SubCommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"subcomments", SubCommentViewSet)


urlpatterns = router.urls

app_name = "app"
