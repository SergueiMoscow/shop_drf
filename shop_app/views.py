from rest_framework import viewsets

from shop_app.models import Product, Category
from shop_app.services import CategorySerializer, ProductSerializer, AdminOrReadOnlyPermission


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrReadOnlyPermission]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnlyPermission]
