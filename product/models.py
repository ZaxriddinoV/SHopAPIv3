from django.core.validators import FileExtensionValidator
from django.db import models

class Products(models.Model):
    MEN = 'men'
    WOMEN = 'women'
    KIDS = 'kids'

    TYPE_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (KIDS, 'Kids'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=MEN)

    product_name = models.CharField(max_length=23)
    description = models.TextField(max_length=300)
    photo = models.CharField(max_length=1000)

    price = models.CharField(max_length=60)

    def __str__(self):
        return self.product_name