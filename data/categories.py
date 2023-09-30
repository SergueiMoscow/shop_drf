import os
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_drf.settings')
django.setup()

from django.utils import timezone
from shop_app.models import Category


# Создаем список категорий
categories = [
    'Фрукты',
    'Овощи',
    'Мясо',
    'Рыба',
    'Хлебобулочные изделия',
    'Кондитерские изделия'
]

# Создаем корневые категории и сохраняем их в базу данных
root_categories = []
for category_name in categories:
    category = Category.objects.create(name=category_name, created_at=timezone.now())
    root_categories.append(category)

# Создаем дополнительные категории с родительскими категориями из списка root_categories
for i in range(20):
    parent_category = random.choice(root_categories)
    category_name = f'{parent_category.name} - подкатегория {i+1}'
    Category.objects.create(name=category_name, created_at=timezone.now(), parent=parent_category)

print('Тестовые данные успешно созданы.')
