from django.http import HttpResponse # Show text on browser
from django.shortcuts import render

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

def aboutUs(request):
    return HttpResponse("<b>Welcome to My Website </b>")

# def course(request):
#     return HttpResponse("Welcome to My Website Course Page")

def courseDetail(request, courseid):
    return HttpResponse(courseid)

## Testing of all Html Pages:
from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')