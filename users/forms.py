from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона', max_length=15, required=False, help_text='Введите номер телефона.')
    username = forms.CharField(label="Никнейм", max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "avatar", "email", "phone", "country")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone



    def __init__(self, *args, **kwargs):
        """Стилизация для регистрации"""
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email@example.com',
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '79876543210',
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Россия',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
        })



class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email"
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "email@example.com",
            "autofocus": True,
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Пароль",
        })