
from rest_framework import viewsets,permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Products, LikeSave

from .serializers import DetailProductSerializer,ProductLikeSerializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

# Create your views here.

class ProductReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = DetailProductSerializer
    queryset = Products.objects.all().order_by()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("product_name", 'description', 'type')
    lookup_field = 'id'

# def like_product(request, product_id):
#     product = get_object_or_404(Products, pk=product_id)
#
#     # Check if the user has already liked this product
#     if ProductLike.objects.filter(user=request.user, product=product).exists():
#         return HttpResponseBadRequest("You have already liked this product.")
#
#         # If the user hasn't liked the product before, create a new Like instance
#     ProductLike.objects.create(user=request.user, product=product)

# class NomViewSet(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = LikeSave.objects.all().order_by()
#     serializer_class = ProductLikeSerializers
#     lookup_field = 'id'


class ProductLikeView(generics.ListCreateAPIView):
    queryset = LikeSave.objects.all()
    serializer_class = ProductLikeSerializers


