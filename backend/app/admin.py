from django.contrib import admin

from app.models import (
    Post,
    Comment,
    SubComment,
)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubComment)
