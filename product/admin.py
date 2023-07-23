from django.contrib import admin
from .models import Products


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','price']

admin.site.register(Products,UserModelAdmin)