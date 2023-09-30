from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop_app.urls')),
    # path('user/', include('users_app.urls')),
]
