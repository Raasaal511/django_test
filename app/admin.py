from django.contrib import admin

from .models import Post, SavePost


admin.site.register(Post)
admin.site.register(SavePost)