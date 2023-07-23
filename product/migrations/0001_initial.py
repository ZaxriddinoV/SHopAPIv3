# Generated by Django 4.2.3 on 2023-07-23 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], default='men', max_length=10)),
                ('product_name', models.CharField(max_length=23)),
                ('description', models.TextField(max_length=300)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staticfiles/product_img/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'pbg', 'heic', 'heif'])])),
                ('price', models.CharField(max_length=60)),
            ],
        ),
    ]