from django.conf import settings
from django.db import models


class Category(models.Model):
    """Модель Категория"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=300, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    """Модель Товар"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=300, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория"
    )
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Владелец",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.category}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["price"]
        permissions = [("can_unpublish_product", "Can unpublish product"),]
