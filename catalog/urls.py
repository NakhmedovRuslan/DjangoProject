from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    home_view,
    contacts,
    submit_form,
    categories,
    choose_category,
    product_detail,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home_view, name="home"),
    path("categories/", categories, name="categories"),
    path("choose_category/", choose_category, name="choose_category"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("contacts/", contacts, name="contacts"),
    path("submit_form/", submit_form, name="submit_form"),
]
