import os
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_drf.settings')
django.setup()

from shop_app.models import Product


products = [
    {"name": "Яблоки", "price": 10, "stock": 200, "category_id": 1},
    {"name": "Морковь", "price": 5, "stock": 100, "category_id": 2},
    {"name": "Свинина", "price": 15, "stock": 300, "category_id": 3},
    {"name": "Тунец", "price": 25, "stock": 800, "category_id": 4},
    {"name":"Булочка с корицей", "price":2, "stock": 50, "category_id":5},
    {"name":"Пирожное с ванилью", "price":4, "stock": 60, "category_id":6},
]

for product_data in products:
    product = Product(name=product_data['name'], price=product_data['price'], category_id=product_data['category_id'])
    product.save()