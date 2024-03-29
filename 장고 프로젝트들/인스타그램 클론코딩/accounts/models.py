from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image_file = ProcessedImageField(
        blank = True,
        upload_to='profile/',
        processors=[ResizeToFit(300,300)],
        format='JPEG',
        options = {'quality':90},
    )