from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'health_status': 'Unknown'})

def profile(request):
    return render(request, 'index.html', {
        'health_status': 'health_status',
        'username': 'username',
        'daily_report': 'daily_report',
        'pending_fields': 'pending_fields'
    })
