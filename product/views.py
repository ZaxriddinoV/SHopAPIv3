
from rest_framework import viewsets,permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Products
from .serializers import DetailProductSerializer

# Create your views here.

class ProductReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = DetailProductSerializer
    queryset = Products.objects.all().order_by()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("product_name", 'description', 'type')
    lookup_field = 'id'






