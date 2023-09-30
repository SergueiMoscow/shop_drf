from django.forms import models
from django.shortcuts import render
from rest_framework import viewsets

from shop_app.models import Product, Category
from shop_app.services import CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
