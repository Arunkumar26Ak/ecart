from django.urls import path, include
from .user.views import user
from .product.views import product
urlpatterns = [
    path('user',user),
    path('product',product),
]
