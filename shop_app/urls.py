from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop_app.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
