from django.db import models

# Create your models here.
class Article(models.Model):
    #title -> char
    title = models.CharField(max_length=10)
    # content -> text
    content = models.TextField()
    # 언제 만들어졌는지
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)