from django.urls import path, include
from .views import signin
urlpatterns = [
    path('signin', signin),
    path('ecart/signin', signin),
    path('',include('apps.ecart.urls')),
]