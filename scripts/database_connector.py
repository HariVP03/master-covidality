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

    for entry in cursor:
        yield entry

def inputData(name, age, initialTemp, finalTemp, emp_id='NULL', feeling=5):

    cursor.execute('SELECT current_timestamp()')
    current_timestamp_obj = cursor.fetchone()
    current_timestamp = str(current_timestamp_obj[0])

    cursor.execute(f'INSERT INTO daily_data VALUES {name, age, initialTemp, finalTemp, emp_id, feeling, current_timestamp}')
    database.commit()

'''
The following line(s) of code are only for testing purposes only.
Please do not un-comment them unnecessarily.

'''


'''
print(database)
print(cursor)

inputData('Test2', 19, 75, 76, '10P21SF1033', 5)

'''



