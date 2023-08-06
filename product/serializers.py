from rest_framework import serializers
from .models import Products,LikeSave

class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id",'type','product_name', 'description', 'photo','price')

class ProductLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikeSave
        fields = ("product_name","user_n")