from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main_view, contact_view, submit_form

app_name = CatalogConfig.name

urlpatterns = [
    path("main/", main_view, name="main"),
    path("contacts/", contact_view, name="contacts"),
    path("submit_form/", submit_form, name="submit_form"),
]