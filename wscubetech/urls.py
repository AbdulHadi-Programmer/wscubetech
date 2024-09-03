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

from django.contrib import admin
from django.urls import path

from wscubetech import views

urlpatterns = [
    # We can change or create urls in this files
    path('', views.HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUs),
    path('course/', views.course),
    # this below will create a dynamic url with only int arg because we already defined it.
    # path('course/<int:courseid>', views.courseDetail),
    # path('course/<slug:courseid>', views.courseDetail),
    # If we dont know any data come on our url then we can leave empty , = to all data types.
    
    # YE HAI ABHI WALA CODE AUE HTML ME FOR LOOP LEARNING KO MAT CHERNA USNE MENE DJANGO K TAGS LIKHAY HOAY HAI .
    path('course/<courseid>', views.courseDetail),
    path('about/', views.aboutUs, name='about'),
    path('services/', views.course, name='services'),
    path('contact/', views.contact, name='contact'),

]
