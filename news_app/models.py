from django.db import models
# from tinymce import HTMLField
from tinymce.models import HTMLField

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_description = HTMLField()