from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product, ProductStockDetails
from .serializers import ProductSerializer, ProductStockDetailsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
from simplecrypt import encrypt, decrypt
from datetime import datetime
from .shopservice import ShopService
from PIL import Image
from io import BytesIO
class ProductAPIView(APIView):

    def get(self, request):
        # object = ShopService()
        productData = ShopService.getProductDetails()
        # productStockData = ShopService.getProductStockDetails()
        print(productData)
        # logindata = Product.objects.raw('Select * from product')
        # serializer = ProductSerializer(logindata,many=True)
        return Response(productData)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            productdata = {"product_id" : obj.product_id}
            request.data.update(productdata)
            print(request.data)
            stockserializer = ProductStockDetailsSerializer(data=request.data)
            if stockserializer.is_valid():
                stockserializer.save()
                data = '{ "data" : "Product Details added Successfully.","status" : "success"}'
                return Response(json.loads(data))
            else:
                data = '{ "data" : "Some Error Occured","status" : "failure"}'
                return Response(json.loads(data))
        else:
            data = '{ "data" : "Some Error Occured","status" : "failure"}'
            return Response(json.loads(data))

@api_view(['GET','POST'])
def product_searchList(request,productname):
    if request.method == 'GET':
        print("Select * from product where product_name LIKE '%"+productname+"%'")
        productData = Product.objects.filter(product_name__contains=productname)
        serializer = ProductSerializer(productData,many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def image_view(request):
    if request.method == 'GET':
        response = "/home/genius/Downloads/Screenshot from 2020-04-17 21-21-47.png"
        img = Image.open(response)
        return HttpResponse(img, content_type="image/png")
        


class ProductAPIDetails(APIView):

    def get_object(self,id):
        try:
            return Product.objects.get(product_id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get_stock_object(self,id):
        try:
            return ProductStockDetails.objects.get(product_id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        product =  self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product =  self.get_object(id)
        productstock =  self.get_stock_object(id)
        serializer = ProductSerializer(product,data=request.data)

        if serializer.is_valid():
            serializer.save()
            productdata = {"product_id" : id}
            request.data.update(productdata)
            print(productstock)
            stockserializer = ProductStockDetailsSerializer(productstock,data=request.data)
            if stockserializer.is_valid():
                stockserializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product =  self.get_object(id)
        productstock =  self.get_stock_object(id)
        product.delete()
        productstock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

       