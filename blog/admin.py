from django.contrib import admin

from .models import BlogPosts


@admin.register(BlogPosts)
class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "views_count")
    list_filter = ("title", "content", "created_at", "views_count")
    search_fields = ("title", "content")
