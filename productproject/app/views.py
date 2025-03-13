from django.shortcuts import render
from .models import Product
from .serializers import Productserializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def Apioverview(req):
    api_urls={
        "all_products":"/AddProductview",
        "add_Product":"/AddProduct",
        "update_product":"/UpdateProduct/update/pk",
        "delete_product":"/product/pk/delete"
    }
    return Response(api_urls)

class AllProductView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializers

class AddProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializers

class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializers
    partial=True
    