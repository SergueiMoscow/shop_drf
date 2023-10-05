from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

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


class AdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method not in ['GET']:
            return request.user.is_superuser
        return True
