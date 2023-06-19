from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','name','descp','price','seller','date','product_active']   

class CustomerSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model= Customer
        fields=['id','name','email','products']           