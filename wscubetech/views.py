## Testing of all Html Pages:
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Import the form file into views
from .forms import *

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
    if request.method == "GET":
        output = request.GET.get('output', None)   # This var used to get the output 
        return render(request, 'about.html', {'output':output})  # Display the var as json

@csrf_exempt
def services(request):
    return render(request, 'services.html')

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
