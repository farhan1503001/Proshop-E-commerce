from django.http.response import JsonResponse
from django.shortcuts import render
from .products import products
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
    return Response(products)
@api_view(['GET'])
def get_product(request,pk):
    product=None
    for item in products:
        if item['_id']==pk:
            product=item
            break
    return Response(product)


