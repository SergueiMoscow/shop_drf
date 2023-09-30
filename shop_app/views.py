from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission

from shop_app.models import Product, Category
from shop_app.services import CategorySerializer, ProductSerializer


class AdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method not in ['GET']:
            return request.user.is_superuser
        return True


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrReadOnlyPermission]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnlyPermission]
