from django.contrib import admin
from .models import Products,LikeSave


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','type','price','id']

admin.site.register(Products,UserModelAdmin)

admin.site.register(LikeSave)