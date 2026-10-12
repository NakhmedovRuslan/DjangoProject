from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("index/", views.ProductListView.as_view(), name="index"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("contacts/", views.SubmitFormView.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(views.ProductDetailView.as_view()), name="product_detail"),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/unpublish/", views.ProductUnpublishView.as_view(), name="product_unpublish"),
    path("categories/<int:category_id>/", views.ProductFilterByCategoryView.as_view(), name="products_filter_by_category"),
]
