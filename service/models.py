# How a Model is Created, When a Project is created then app is created
# in model file we create that model and run some commands

 
# python manage.py makemigrations
# python manage.py migrate


from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_description = models.TextField()

# After Creating the model , run the two migrations command
