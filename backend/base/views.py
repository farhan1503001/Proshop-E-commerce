from .serializers import Product_serializer
from django.http.response import JsonResponse
from django.shortcuts import render
from .products import products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
# Create your views here.
@api_view(['GET','POST'])
def getRoutes(request):
    routes=['apps',
    '/apps/products/',
    '/apps/products/create/',
    '/apps/products/upload/',
    '/apps/products/<id>/reviews/',
    '/apps/products/top',
    '/api/products/<id>'
    ]
    return Response(routes)

@api_view(['GET'])
def get_products(request):
    products=Product.objects.all()
    serializer=Product_serializer(products,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_product(request,pk):
    product=Product.objects.get(_id=pk)
    serializer=Product_serializer(product,many=False)
    return Response(serializer.data)


