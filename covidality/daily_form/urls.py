from django.urls import path
from . import views

# Redirecting the 'fill_form' action specified in the <form> to views.py and executing the function fill_form
urlpatterns = [
    path('daily_form', views.fill_daily_form, name='fill_form'),
    path('fill_form', views.fill_form),
    path('loginForm', views.loginForm),
    path('login', views.login)
]