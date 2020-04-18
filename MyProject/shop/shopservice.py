from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
import json

class ShopService:
    def getShopDetails():
        logindata = Product.objects.raw('Select * from product')
        serializer = ProductSerializer(logindata,many=True)
        return serializer.data