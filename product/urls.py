from django.urls import path
from rest_framework.routers import DefaultRouter

from product.views import ProductLikeView

from .views import ProductReviewsViewSet

app_name = "product"


router = DefaultRouter()

router.register('',ProductReviewsViewSet,basename='reviews'),





urlpatterns = [
    path('api/likes/', ProductLikeView.as_view(), name='product-like-list-create'),
]
urlpatterns += router.urls