from django.urls import path, include
from .views import CustomAuthToken, UserCreateView, UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet)

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('register/', UserCreateView.as_view()),
    path('', include(router.urls)),
]
