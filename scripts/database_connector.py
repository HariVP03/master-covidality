import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='covidality'
)

cursor = database.cursor()


def getDailyData():
    cursor.execute('SELECT * FROM daily_data')
    entries = list()
    for entry in cursor.fetchall():
        entries.append(entry)
    return entries

def inputData(name, age, initialTemp, finalTemp, emp_id='NULL', feeling=5):

    # Getting the timestamp (date, time) at the time of data entry
    # and entering it in the time_stamp column
    cursor.execute('SELECT current_timestamp()')
    current_timestamp_obj = cursor.fetchone()
    current_timestamp = str(current_timestamp_obj[0])

    cursor.execute(f'INSERT INTO daily_data VALUES {name, age, initialTemp, finalTemp, emp_id, feeling, current_timestamp}')
    database.commit()

def debug():

    if input('Command: ') == 'get_data':
        print(getDailyData())

    else:
        name = input('Name: ')
        age = input('Age: ')
        initialTemp = input('Initial Temperature: ')
        finalTemp = input('Final Temperature: ')
        emp_id = input('Employee ID: ')
        feeling = input('Feeling: ')

        inputData(name, age, initialTemp, finalTemp, emp_id, feeling)


