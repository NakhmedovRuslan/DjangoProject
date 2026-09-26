from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import BlogPosts


class BlogPostsListView(ListView):
    """Контроллер просмотра списка блогов"""
    model = BlogPosts
    template_name = "blogposts_list.html"

    def get_queryset(self):

        return BlogPosts.objects.filter(is_published=True)


class BlogPostsDetailView(DetailView):
    """Контроллер подробного чтения конкретного блога с счётчиком просмотра"""
    model = BlogPosts
    template_name = "blog/blogposts_detail.html"
    context_object_name = "blogposts"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostsCreateView(CreateView):
    """Контроллер создания нового блога"""
    model = BlogPosts
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogposts_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogPostsUpdateView(UpdateView):
    """Контроллер редактирования ранее созданного блога"""
    model = BlogPosts
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogposts_form.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", args={self.kwargs["pk"]})


class BlogPostsDeleteView(DeleteView):
    """Контроллер удаления ранее созданного блога"""
    model = BlogPosts
    template_name = "blog/blogposts_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
