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
    prediction = predictedData[-1][1]
    health_status = 'To Be Evaluated'

    try:
        data1 = dailyData[-1]
    except:
        data1 = [' ' for _ in range(7)]
    try:
        data2 = dailyData[-2]
    except:
        data2 = [' ' for _ in range(7)]
    try:
        data3 = dailyData[-3]
    except:
        data3 = [' ' for _ in range(7)]
    try:
        data4 = dailyData[-4]
    except:
        data4 = [' ' for _ in range(7)]
    try:
        data5 = dailyData[-5]
    except:
        data5 = [' ' for _ in range(7)]

    data1_str = f'Temperature 1: {data1[2]}, Temperature 2: {data1[3]}, Feeling: {data1[5]}, Time: {data1[6]}'
    data2_str = f'Temperature 1: {data2[2]}, Temperature 2: {data2[3]}, Feeling: {data2[5]}, Time: {data2[6]}'
    data3_str = f'Temperature 1: {data3[2]}, Temperature 2: {data3[3]}, Feeling: {data3[5]}, Time: {data3[6]}'
    data4_str = f'Temperature 1: {data4[2]}, Temperature 2: {data4[3]}, Feeling: {data4[5]}, Time: {data4[6]}'
    data5_str = f'Temperature 1: {data5[2]}, Temperature 2: {data5[3]}, Feeling: {data5[5]}, Time: {data5[6]}'

    return render(request, 'index.html', {
        'health_status': health_status,
        'username': username,
        'prediction': prediction,
        'recent_input1': data1_str,
        'recent_input2': data2_str,
        'recent_input3': data3_str,
        'recent_input4': data4_str,
        'recent_input5': data5_str,
    })

def table(request):

    return render(request, 'loginTable.html')

def html_format_table(temp1, temp2, feeling, time):

    temp1.reverse()
    temp2.reverse()
    feeling.reverse()
    time.reverse()

    html_code = ''
    for i in range(0, len(temp1)):
        html_code += f'<tr> <td>{temp1[i]}</td><td>{temp2[i]}</td><td>{feeling[i]}</td><td>{time[i]}</td></tr>'
    return html_code

def loginTable(request):
    emp_id = request.POST.get('emp_id')
    password = request.POST.get('password')

    temp1 = list()
    temp2 = list()
    feeling = list()
    time = list()

    dailyData = getDailyData(emp_id)
    username = dailyData[0][0]
    html_code = list()
    for entry in dailyData:
        temp1.append(entry[2])
        temp2.append(entry[3])
        feeling.append(entry[5])
        time.append(entry[6])

    html_code.append(html_format_table(temp1, temp2, feeling, time))

    table_data = ''.join(html_code)
    print(getPrediction('10p21sf1033'))
    return render(request, 'table.html', {
        'table_data': table_data,
        'username': username
    })

