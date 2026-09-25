from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар",]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]

    def clean_name(self):
        """Проверка наличия запрещенных слов в названии"""
        name = self.cleaned_data["name"]

        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(
                    "В названии используются запрещенные слова"
                )

        return name

    def clean_description(self):
        """Проверка наличия запрещенных слов в описании"""
        description = self.cleaned_data["description"]

        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(
                    "В описании используются запрещенные слова"
                )

        return description

    def clean_price(self):
        """Проверка цены"""
        price = self.cleaned_data["price"]

        if price <= 0:
            raise ValidationError(
                "Цена должна быть положительным числом."
            )

        return price

    def clean_image(self):
        """Проверка изображения, не более 5мб и расширение"""
        image = self.cleaned_data["image"]

        if image.size > 5 * 1024 * 1024:
            raise ValidationError(
                "Размер изображения не должен превышать 5 МБ."
            )

        if image.content_type not in ["image/jpeg", "image/png"]:
            raise ValidationError(
                "Можно загружать только изображения в формате JPEG или PNG"
            )

        return image


    def __init__(self, *args, **kwargs):
        """Стилизация"""
        super(ProductForm, self).__init__(*args, **kwargs)


        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })


        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })


        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
