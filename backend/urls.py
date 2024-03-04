from rest_framework.routers import DefaultRouter
from app.views import PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)


urlpatterns = router.urls

app_name = "app"
