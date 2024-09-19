from django.contrib import admin
from news_app.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title', 'news_description')

admin.site.register(News, NewsAdmin)