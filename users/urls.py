from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:index"), name="logout"),
]
