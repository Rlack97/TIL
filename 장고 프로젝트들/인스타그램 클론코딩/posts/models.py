from distutils.command.upload import upload
from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='image/',
        null=True,
        )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  related_name='posts', on_delete=models.CASCADE,)