"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
### Three types of value we can sent:
1. int, 2. str, 3. slug

"""

from wscubetech import views
from django.contrib import admin
from django.urls import path
from wscubetech import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.aboutUs, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('userform/',views.userform, name='userform'),
    path('submitform/',views.submitform, name='submitform'),
    path('calculator/', views.calculator, name='calculator'),
    path('evenodd/', views.evenodd, name='evenodd'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('home/', views.NewPage, name="new"),

]