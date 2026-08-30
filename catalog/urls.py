from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_view, contact_view, submit_form

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home_view, name="home"),
    path("contacts/", contact_view, name="contacts"),
    path("submit_form/", submit_form, name="submit_form"),
]