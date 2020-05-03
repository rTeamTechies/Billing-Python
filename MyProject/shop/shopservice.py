from rest_framework.parsers import JSONParser
from .models import Product, ProductStockDetails
from .ShopModels import ShopDetails, ShopContactDetails
from .serializers import ProductSerializer, ShopDetailsSerializer, ProductStockDetailsSerializer, ShopContactDetailsSerializer
import json

class ShopService:
    def getProductDetails():
        productdata = Product.objects.raw('Select * from product')
        serializer = ProductSerializer(productdata,many=True)
        return serializer.data
        
    def getShopDetails():
        shopdata = ShopDetails.objects.raw('Select * from shop_dtls')
        serializer = ShopDetailsSerializer(shopdata,many=True)
        return serializer.data

    def getShopContactDetails():
        shopdata = ShopContactDetails.objects.raw('Select * from shop_contact_dtls')
        serializer = ShopContactDetailsSerializer(shopdata,many=True)
        return serializer.data

    def getProductStockDetails():
        productdata = Product.objects.raw('Select * from product')
        serializer = ProductSerializer(productdata,many=True)
        return serializer.data

        