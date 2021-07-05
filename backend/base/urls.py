from .views import get_product, get_products
from base.views import getRoutes
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('',getRoutes,name='home'),
    path('products/',get_products,name='products'),
    path('products/<str:pk>',get_product,name='product'),
]