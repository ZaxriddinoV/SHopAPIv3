from rest_framework import serializers
from .models import Products

class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id",'type','product_name', 'description', 'photo','price')

