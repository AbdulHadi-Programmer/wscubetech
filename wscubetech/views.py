## Testing of all Html Pages:
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def HomePage(request):
    # data = {
    #     'title' : 'Home Page',
    #     'bdata': 'Hello I am a Developer',
    #     'clist': ['python', 'js', 'java', 'c', 'go', 'dart'],
    #     # 'numbers' : [],
    #     'numbers' : [11, 22, 33, 44, 55, 66],
    #     'student_detail': [
    #         {'name': 'Student 1', 'age': 19},
    #         {'name': 'Student 2', 'age': 29}
    #     ]
    # }
    return render(request, "index.html")

@csrf_exempt
def HomePage(request):
    return render(request, 'index.html')

@csrf_exempt
def aboutUs(request):
    return render(request, 'about.html')

@csrf_exempt
def services(request):
    return render(request, 'services.html')

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')