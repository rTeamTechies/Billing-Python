from rest_framework import serializers
from .models import Product
from .ShopModels import ShopDetails, ShopContactDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShopDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetails
        fields = '__all__'

class ShopContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopContactDetails
        fields = '__all__'