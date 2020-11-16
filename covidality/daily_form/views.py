from django.shortcuts import render


def fill_daily_form(request):
    return render(request, 'daily form.html')

# The action attribute in <form> tag of daily_form.html page is connected to the urls.py of this
# app. The urls.py of this app redirects it here
def fill_form(request):
    name = request.POST['name']
    age = request.POST['age']
    temp1 = request.POST['temp1']
    temp2 = request.POST['temp2']
    emp_id = request.POST['emp_id']
    feeling = request.POST['feeling']

    return render(request, 'submission-received.html')
