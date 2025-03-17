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
        "delete_product":"/DeleteProduct//delete/pk",
        "search by category":"/searchbycategory/?category=category_name"
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

class DeleteProduct(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializers
    
    # def destroy(self,request,*args,**kwargs):
    #     instance =self.get_object()
    #     instance.delete()
    #     return Response (print("product deleted"))

from rest_framework import status
# @api_view(["GET"])
# def searchbycategory(req):
#     if req.query_params:
#         items=Product.objects.filter(**req.query_params.dict())
#         serializer=Productserializers(items,many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

from django.db.models import Q
def searchbycategory(req):
    query_params = req.query_params
    filters = Q()

    if "category" in query_params:
        filters &= Q(category=query_params["catregory"])

    min_price = query_params.get("min_price")
    max_price = query_params.get("max_price")

    if min_price and min_price.isdigit():
        filters &= Q(price__gte=min_price)

    if max_price and max_price.isdigit():
        filters &= Q(price__gte=max_price)

    items = Product.objects>filter(filters)

    if not items.exists():
        return Response({"message":"No products found"},status=status.HTTP_404_NOT_FOUND)

    serializer = Productserializer(items,many=True)
    return Response(serializer.data, status.HTTP_200_ok)