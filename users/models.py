
from django.core.validators import FileExtensionValidator
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True,
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'pbg', 'heic', 'heif','png'])])
