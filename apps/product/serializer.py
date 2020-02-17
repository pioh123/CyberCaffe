from rest_framework import serializers
from .models import Product, Advertise

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','photo','stock','price')


class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = ('id','name','image','description','typea')


