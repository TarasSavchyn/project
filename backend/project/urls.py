from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # path("api/app/", include("app.urls", namespace="app")),
    path("api/user/", include("user.urls", namespace="user")),

]
