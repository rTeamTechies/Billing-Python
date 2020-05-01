from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .ShopModels import ShopDetails, ShopContactDetails
from .serializers import ShopDetailsSerializer, ShopContactDetailsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
from simplecrypt import encrypt, decrypt
from datetime import datetime
from .shopservice import ShopService

class ShopDetailsAPIView(APIView):

    def get(self, request):
        productData = ShopService.getShopDetails()
        return Response(productData)

    def post(self, request):
        serializer = ShopDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = '{ "data" : "Shop Details added Successfully.","status" : "success"}'
            return Response(json.loads(data))
        else:
            data = '{ "data" : "Some Error Occured","status" : "failure"}'
            return Response(json.loads(data))

class ShopContactDetailsAPIView(APIView):

    def get(self, request):
        productData = ShopService.getShopContactDetails()
        return Response(productData)

    def post(self, request):
        print(request.data)
        serializer = ShopContactDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = '{ "data" : "Shop Contact Details added Successfully.","status" : "success"}'
            return Response(json.loads(data))
        else:
            data = '{ "data" : "Some Error Occured","status" : "failure"}'
            return Response(json.loads(data))


class ShopAPIDetails(APIView):

    def get_object(self,id):
        try:
            return ShopDetails.objects.get(shop_id=id)
        except ShopDetails.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        shop =  self.get_object(id)
        serializer = ShopDetailsSerializer(shop)
        return Response(serializer.data)

    def put(self, request, id):
        shop =  self.get_object(id)
        serializer = ShopDetailsSerializer(shop,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        shop =  self.get_object(id)
        shop.delete()
        data = '{ "data" : "Shop Details deleted Successfully.","status" : "success"}'
        return Response(json.loads(data))


class ShopContactDetailsAPI(APIView):

    def get_object(self,id):
        try:
            return ShopContactDetails.objects.get(shop_id=id)
        except ShopContactDetails.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        shop =  self.get_object(id)
        serializer = ShopContactDetailsSerializer(shop)
        return Response(serializer.data)

    def put(self, request, id):
        shop =  self.get_object(id)
        serializer = ShopContactDetailsSerializer(shop,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        shop =  self.get_object(id)
        shop.delete()
        data = '{ "data" : "Shop Contact Details deleted Successfully.","status" : "success"}'
        return Response(json.loads(data))