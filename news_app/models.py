from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_description = HTMLField()

    # slug add title to the url with this popular 
    news_slug = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None)
    # news_slug make the title with lower case and each is separated with - and for applying this we have to go on admin before that apply migrations and then click on each news then save and also change the views and urls file so that each setting is properly is set to show , now the slug is show on url on website

