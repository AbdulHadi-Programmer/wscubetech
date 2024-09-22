## Testing of all Html Pages:
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from service.models import Service
from news_app.models import News

# @csrf_exempt
# def HomePage(request):
#     # Now we are getting data from database and render it on html page.
#     servicesData = Service.objects.all() # object is a class
#     # for a in servicesData:
#     #     print(a.service_icon, "\n\n\n")
#     print(servicesData)
#     # data = {
#     #     'servicesData': servicesData
#     # }
#     # servicesData = 'servicesData'
#     # for service in servicesData:
#     #     print(service.title, service.description)
 
#     # data = {
#     #     'title' : 'Home Page',
#     #     'bdata': 'Hello I am a Developer',
#     #     'clist': ['python', 'js', 'java', 'c', 'go', 'dart'],
#     #     # 'numbers' : [],
#     #     'numbers' : [11, 22, 33, 44, 55, 66],
#     #     'student_detail': [
#     #         {'name': 'Student 1', 'age': 19},
#     #         {'name': 'Student 2', 'age': 29}
#     #     ]
#     # }
#     return render(request, "index.html", {'servicesData': servicesData})

@csrf_exempt
def NewPage(request):
    # Fetch all services from the database
    servicesData = Service.objects.all() 

    # Pass servicesData directly to the template
    return render(request, "new.html", {'servicesData': servicesData})



@csrf_exempt
def HomePage(request):
    newsData = News.objects.all()
    
    return render(request, 'index.html', {'newsData': newsData})

@csrf_exempt
def newsDetail(request, news_id):
    try:
        newsDetail = News.objects.get(id=news_id) 
        # .get is used to get single paramenter and it required id and we give news_id that is connected to each news 
    except News.DoesNotExist:
        # Handle the case where the news does not exist (you can render a 404 or redirect)
        return HttpResponse('News item not found', status=404)
    
    return render(request, "newsdetails.html", {'newsDetail': newsDetail})


@csrf_exempt
def aboutUs(request):
    if request.method == "GET":
        output = request.GET.get('output', None)   # This var used to get the output 
        return render(request, 'about.html', {'output':output})  # Display the var as json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Service  # Assuming Service model is defined

@csrf_exempt
def services(request):
    serviceData = Service.objects.all()
    
    if request.method == 'GET':
        st = request.GET.get('servicename')  # Capture search query
        if st:  # Only filter if there's a search query
            serviceData = Service.objects.filter(service_title__icontains=st)  # Use icontains for partial matches
    
    data = {
        'serviceData': serviceData,
    }
    
    return render(request, 'services.html', data)

@csrf_exempt
def new(request):
    serviceData = Service.objects.all()
    
    if request.method == 'GET':
        st = request.GET.get('servicename')  # Capture search query
        if st:  # Only filter if there's a search query
            serviceData = Service.objects.filter(service_title__icontains=st)
    data = {
        'serviceData': serviceData,
    }
    return render(request, 'new.html', data)

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')

# 1st ways to use csrf token and 2nd way is in html file

@csrf_exempt  # Only use this for development/testing purposes; it's insecure in production
def userform(request):
    fn = UserForm()
    data = {'form':fn}
    try:
        if request.method == "POST":
            # n1 = int(request.GET['num1'])  # This is the 1st way to take data input
            # n2 = int(request.GET['num2']) 
            # Retrieve data from the POST request
            n1 = int(request.POST.get('num1', 0))  # Default to 0 if no input
            n2 = int(request.POST.get('num2', 0))  # Default to 0 if no input
            result = n1 + n2

            # Send the result back to the template
            data = {
            #     'n1': n1,
            #     'n2': n2,
                'form':fn,
                'result': result,  # Use 'result' to display the sum
            }
            # Now After redirecting the url var display about page with the output var
            # Because after filling the input then click save the about page displayed 
            # and result is shown in link format given below
            url = f'/about/?output={result}'
        # We can also display the result on new page 

            # This below line is used to redirect form page to about as when form is save/submit then it will show about page
            return HttpResponseRedirect(url)

    except Exception as e:
        print(f"Error: {e}")
        data['error'] = "An error occurred during calculation."

    # Render the form and display the result if POST request was successful
    return render(request, 'userform.html', data)

# Action is used to submit the form on the given url, see this in userform
# and if action is not given then it take the current url to submit that
def submitform(request):
    data = {}

    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1', 0))  # Default to 0 if no input
            n2 = int(request.POST.get('num2', 0))  # Default to 0 if no input
            result = n1 + n2

            # Send the result back to the template
            data = {
                'n1': n1,
                'n2': n2,
                'result': result,  # Use 'result' to display the sum
            }
            # Now this is display the result on submit form page and 
            return HttpResponse(result)
    
    except:
        pass

@csrf_exempt
def calculator(request):
    c = 0
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2 
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2

    except Exception as e:
        c = "Invalid Operation"
    print(c)
    return render(request, 'calculator.html', {'c':c}) # The c is send to html file and it will be easily used


# @csrf_exempt
# def evenodd(request):
#     try:
#         c = ''
#         if request.method == "POST":
#             if request.POST.get('num1'):
#                 return render(request, "evenodd.html", {"error": True})
#             n = int(request.POST.get('num1'))
#             if n % 2 == 0:
#                 c = 'Even'
#             elif n % 2 != 0:
#                 c = 'Odd'
            
#             return render(request, "evenodd.html", {"c": c})
            
#     except ValueError:
#         c = 'Invalid Input'
        
#     return render(request, 'evenodd.html', {'c':c})
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def evenodd(request):
    c = ''
    try:
        if request.method == "POST":

            # If num1 is not provided, show error
            if request.POST.get('num1')=="":
                return render(request, "evenodd.html", {"error": True})#, "message": "Number is required"})

            num1 = request.POST.get('num1')
            # Try to convert num1 to integer
            n = int(num1)

            if n % 2 == 0:
                c = 'Even'
            else:
                c = 'Odd'
            
            return render(request, "evenodd.html", {"c": c})

    except ValueError:
        # Handle invalid integer input
        c = 'Invalid Input'

    return render(request, 'evenodd.html', {'c': c})



@csrf_exempt
def marksheet(request):
    if request.method == 'POST':
        subject1 = int(request.POST.get('subject1', 0)) # Get the value from html file 
        subject2 = int(request.POST.get('subject2', 0))
        subject3 = int(request.POST.get('subject3', 0))
        subject4 = int(request.POST.get('subject4', 0))
        subject5 = int(request.POST.get('subject5', 0))

        # Calculate the total and percentage :
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100

        # Determine division based on percentage 
        if percentage >= 85:
            division = 'First Division'
        elif percentage >= 70:
            division = 'Second Division'
        elif percentage >= 60:
            division = 'Third Division'
        elif percentage >= 50:
            division = 'Fourth Division'
        elif percentage >= 40:
            division = 'Five Division'
        else: 
            division = 'Fail'

        # pass the data back to the template 
        return render(request, 'marksheet.html', {
            'total':total,
            'percentage':percentage,
            'division':division
        })
    return render(request, 'marksheet.html')
