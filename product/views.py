from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated

from .models import Products
from .serializers import DetailProductSerializer

# Create your views here.

class ProductReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = DetailProductSerializer
    queryset = Products.objects.all().order_by()
    lookup_field = 'id'