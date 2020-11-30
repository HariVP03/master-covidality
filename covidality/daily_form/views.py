from django.shortcuts import render

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='covidality'
)

cursor = database.cursor()

def inputData(name, age, initialTemp, finalTemp, emp_id='NULL', feeling=5):

    # Getting the timestamp (date, time) at the time of data entry
    # and entering it in the time_stamp column
    cursor.execute('SELECT current_timestamp()')
    current_timestamp_obj = cursor.fetchone()
    current_timestamp = str(current_timestamp_obj[0])

    cursor.execute(f'INSERT INTO daily_data VALUES {name, age, initialTemp, finalTemp, emp_id, feeling, current_timestamp}')
    database.commit()

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

    inputData(name, age, temp1, temp2, emp_id, feeling)

    return render(request, 'submission-received.html')
