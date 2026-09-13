from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("index/", views.BlogPostsListView.as_view(), name="blog_list"),
    path("blog/create/", views.BlogPostsCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/", views.BlogPostsDetailView.as_view(), name="blog_detail"),
    path(
        "blog/<int:pk>/update/", views.BlogPostsUpdateView.as_view(), name="blog_update"
    ),
    path(
        "blog/<int:pk>/delete/", views.BlogPostsDeleteView.as_view(), name="blog_delete"
    ),
]
