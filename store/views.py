from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.relations import PKOnlyObject
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer


@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
