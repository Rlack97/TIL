from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='image/',
        blank=True,
        null=True,
        )