import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1qaz2wsx',
    database='covidality'
)

cursor = database.cursor()

def getDailyData():
    cursor.execute('SELECT * FROM daily_data')

    for entry in cursor:
        yield entry

def inputData(name, age, initialTemp, finalTemp, feeling, time_stamp='', emp_id='Null'):
    cursor.execute(f'INSERT INTO daily_data VALUES {name, age, initialTemp, finalTemp, feeling, time_stamp, emp_id}')


'''
The following line(s) of code are only for testing purposes only.
Please do not un-comment them unnecessarily.

'''

'''

print(database)
print(cursor)

'''
inputData('Test2', 20, 99, 101, 9)