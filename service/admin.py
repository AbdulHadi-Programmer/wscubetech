from django.contrib import admin
from service.models import Service
# Register your models here.

# This file and this below class creating a new tab name "service" in admin panel
# Add the function on admin page by using this class and "admin.ModelAdmin" is used to take permission 
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon', 'service_title', 'service_description')  # This display the fields

# 1st us the function or main thing to add and 2nd is class 
admin.site.register(Service, ServiceAdmin)