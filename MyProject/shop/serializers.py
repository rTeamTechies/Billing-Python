from rest_framework import serializers
from .models import Product, ProductStockDetails
from .ShopModels import ShopDetails, ShopContactDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductStockDetailsSerializer(serializers.ModelSerializer):
    stock = ProductSerializer(read_only = True)
    class Meta:
        model = ProductStockDetails
        fields = '__all__'

class ShopDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetails
        fields = '__all__'

class ShopContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopContactDetails
        fields = '__all__'