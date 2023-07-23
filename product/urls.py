from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductReviewsViewSet



app_name = "product"


router = DefaultRouter()
router.register('',ProductReviewsViewSet,basename='reviews')
urlpatterns = router.urls
