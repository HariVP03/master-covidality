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

def getDailyData(emp_id):
    cursor.execute(f"SELECT * FROM daily_data WHERE emp_id = '{emp_id}'")
    entries = list()
    for entry in cursor.fetchall():
        entries.append(entry)
    return entries

def getPrediction(emp_id):
    cursor.execute(f"SELECT daily.emp_id, pred.predictedFinalTemp FROM daily_data daily, predictions pred WHERE daily.emp_id = pred.emp_id AND daily.emp_id = '{emp_id}'")
    entries = list()
    for entry in cursor.fetchall():
        entries.append(entry)
    return entries

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

def loginForm(request):
    return render(request, 'login.html')

def login(request):

    emp_id = request.POST.get('emp_id')
    password = request.POST.get('password')

    dailyData = getDailyData(emp_id)
    predictedData = getPrediction(emp_id)

    username = dailyData[0][0]
    prediction = predictedData[0][1]
    health_status = 'To Be Evaluated'
    pending_fields = 'None'

    return render(request, 'index.html', {
        'health_status': health_status,
        'username': username,
        'prediction': prediction,
        'pending_fields': pending_fields
    })