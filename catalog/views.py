from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.models import Category, Product


class IndexView(TemplateView):
    template_name = "base.html"


class SubmitFormView(View):
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


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories.html"
    context_object_name = "categories"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/main.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    fields = ["name", "description", "price", "category", "image"]
    success_url = reverse_lazy("catalog:index")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    fields = ["name", "description", "price", "category", "image"]
    context_object_name = "product"
    success_url = reverse_lazy("catalog:index")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args={self.kwargs["pk"]})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:index")
