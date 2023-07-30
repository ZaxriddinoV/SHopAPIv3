from django.contrib import admin
from .models import Products


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','type','price','id']

admin.site.register(Products,UserModelAdmin)