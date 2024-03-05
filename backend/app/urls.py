from rest_framework.routers import DefaultRouter
from app.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)


urlpatterns = router.urls

app_name = "app"
