from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField("Телефон", max_length=15, blank=True, null=True)
    avatar = models.ImageField("Аватар профиля", upload_to='avatars/', blank=True, null=True)
    country = models.CharField("Страна", max_length=25, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email