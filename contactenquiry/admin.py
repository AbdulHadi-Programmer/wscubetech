from django.contrib import admin
from .models import *

class EnquirySave(admin.ModelAdmin):
    list_display=('name', 'email', 'message')

admin.site.register(contactEnquiry, EnquirySave)
