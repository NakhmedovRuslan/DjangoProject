from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product


class IndexView(TemplateView):
    """контроллер базового шаблона"""
    template_name = "base.html"


class SubmitFormView(View):
    """Контроллер кнопки "отправить" на странице контактов"""
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        html_content = """
        <html>
        <body>
        <h1>Спасибо за обратную связь!</h1>
        </body>
        </html>
        """
        return HttpResponse(html_content)


class CategoryListView(LoginRequiredMixin, ListView):
    """Контроллер списка категорий (просмотр)"""
    model = Category
    template_name = "catalog/categories.html"
    context_object_name = "categories"


class ProductListView(ListView):
    """Контроллер списка товаров"""
    model = Product
    template_name = "catalog/main.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер подробного просмотра товара"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания нового товара"""
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер редактирования товара, права только у владельца"""
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    context_object_name = "product"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.kwargs["pk"]])

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.is_superuser:
            raise PermissionDenied("Вы не владелец этого товара")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления товара, только владелец или модератор"""
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:index")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.has_perm("catalog.delete_product")

        if not (is_owner or is_moderator):
            raise PermissionDenied("Вы не имеете доступ (не владелец и не модератор)")
        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(LoginRequiredMixin, View):
    """Отмена публикации (только для модератора)"""

    def post(self, request, pk):
        if not request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Нет права can_unpublish_product")

        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect("catalog:product_detail", pk=pk)