from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Category.objects.all().delete()
        category_phones, _ = Category.objects.get_or_create(name='Телефоны')
        category_notebooks, _ = Category.objects.get_or_create(name='Ноутбуки')

        products = [
            {'name': 'ASUS', 'description': 'Игровой ноутбук', 'price': '99100.56', 'category': category_notebooks},
            {'name': 'ACER', 'description': 'oled экран', 'price': '69105.00', 'category': category_notebooks},
            {'name': 'Lenovo', 'description': 'Создан для работы', 'price': '89000.00', 'category': category_notebooks},
            {'name': 'Iphone', 'description': 'Лучшая камера', 'price': '89000.00', 'category': category_phones},
            {'name': 'Xiomi', 'description': 'Для игр', 'price': '59000.00', 'category': category_phones},
            {'name': 'Samsung', 'description': 'Лучший экран', 'price': '99000.00', 'category': category_phones}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))