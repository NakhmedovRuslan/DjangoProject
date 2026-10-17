from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """Получает данные по товарам из кэша. Если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, timeout=60)
    return products



def filter_products_by_category(category_id):
    """Функция фильтрует список товаров на товары конкретной категории"""
    filtered_products = Product.objects.filter(category=category_id)
    return filtered_products


