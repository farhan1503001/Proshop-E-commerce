from django.http.response import JsonResponse
from django.shortcuts import render
from .products import products
# Create your views here.
def getRoutes(request):
    routes=['apps',
    '/apps/products/',
    '/apps/products/create/',
    '/apps/products/upload/',
    '/apps/products/<id>/reviews/',
    '/apps/products/top',
    '/api/products/<id>'
    ]
    return JsonResponse(routes,safe=False)
def get_products(request):
    return JsonResponse(products,safe=False)
def get_product(request,pk):
    product=None
    for item in products:
        if item['_id']==pk:
            product=item
            break
    return JsonResponse(product,safe=False)


