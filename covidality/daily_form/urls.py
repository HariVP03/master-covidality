from django.urls import path
from . import views

# Redirecting the 'fill_form' action specified in the <form> to views.py and executing the function fill_form
urlpatterns = [
    path('form/daily_form', views.fill_daily_form, name='fill_form'),
    path('form/fill_form', views.fill_form),
    path('loginForm', views.loginForm),
    path('login', views.login),
    path('table', views.table),
    path('loginTable', views.loginTable)
]

handler404 = 'daily_form.views.custom_404'
handler500 = 'daily_form.views.custom_500'