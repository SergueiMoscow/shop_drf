from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop_app.models import Category, Product


class IsSuperuser:
    pass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
