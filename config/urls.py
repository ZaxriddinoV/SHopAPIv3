
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="E-SHOP Api",
        description="E-SHOP Api uchun qollanma ",
        default_version='v2',
        terms_of_service='https://www.google.com/policies/terms/',
        contact= openapi.Contact(email='zaxriddinov1707@gmail.com'),
        license=openapi.License(name="E-SHop license"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf/',include('rest_framework.urls')),
    path('users/', include("users.urls")),
    path("product/", include("product.urls")),


    path("", schema_view.with_ui(
        'swagger', cache_timeout=0),name="swagger")

]