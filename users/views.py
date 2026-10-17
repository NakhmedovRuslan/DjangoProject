import os

from django.contrib.auth.views import LoginView
from dotenv import load_dotenv



load_dotenv(override=True)

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.core.mail import send_mail

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = "Добро пожаловать в интернет магазин!"
        message = "Спасибо за регистрацию в нашем интернет магазине"
        from_email = os.getenv("EMAIL_HOST_USER")
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("catalog:index")