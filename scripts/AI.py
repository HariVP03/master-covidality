''' 

This is the Official Covidality AI code.

Class 12 computer project by Harsh Vardhan Shukla and Hari Vishnu Parashar

Please Use the Following Format for Inputting Data:

temp_final: [[t1i, t1f], [t2i, t2f], ...]
howBadDoYouFeel: List of integers from 1-10
predict_case: [initial temperature, howBadAreYouFeeling]

'''

# The main library for the AI
from sklearn import tree

# Python file which establishes a connection to MySQL using the Python connector
import database_connector as db

def AI(temp_list, howBadDoYouFeel, predict_case):

    # Initialising some variables
    init_templist = list()
    final_templist = list()

    trainX = list()
    trainY = list()

    # Evaluates and returns 1 for feeling BAD(>=5) and 0 for feeling FINE
    def evaluateFeel(howBadDoYouFeel):

        if howBadDoYouFeel>=5:
            feelingBool = 1
        else:
            feelingBool = 0
        return feelingBool

    # Unpacking initial and final temperatures in the list to a new liswt for ease of access later
    for init_temp, final_temp in temp_list:

        init_templist.append(init_temp)
        final_templist.append(final_temp)

    # Assigning X Values for the data
    # These values are of the form: [ ... [initial_temperature, feeling_boolean] ... ]
    # These values will be given when prediction is required
    for i in range(len(init_templist)):

        init_temp_element = init_templist[i]
        feeling_element = evaluateFeel(howBadDoYouFeel[i])

        trainX.append([init_temp_element, feeling_element])

    # Assigning Y Values for the data
    # These values are of the form: [..., final_temperature, ...]
    # THese values will be predicted. For prediction the Y Values are required
    trainY = final_templist

    # Initialising the Tree Decision AI
    classifier = tree.DecisionTreeClassifier()

    # Training the AI with previously collected data
    classifier.fit(trainX, trainY)

    # Finally return the prediction based on the training data and the prediction's X Values
    return classifier.predict(predict_case)

def test():

    try:
        # Initial Temperature, Final Temperature
        features = [[1, 2], [2, 9], [3, 5], [5, 6]]
        # How Bad are you Feeling?
        labels = [9, 5, 4, 11]
        # Here 2 is the initial temperature and 10 is how bad you are feeling
        predict_this = [[1, 6]]

        # Initial Temperature, Feeling ELement
        print(AI(features, labels, predict_this))

    except:

        raise ReferenceError

# Function that counts the number of unique items in a list
# This is used to find the number of people who filled their forms that month
def count_unique(array):
    count = 0
    for item in array:
        if array.count(item) == 1:
            count += 1
    return count

# Function that runs the script
# It will get the data from the database using database_connector.
# This function needs to be executed ONLY AT THE END OF THE MONTH
# because it uses the data collected that month to train the AI and make
# further predictions
def run():
    command = input('Command: ')
    if command == 'generate_report':
        employee_id = list()

        # Connects to the database_connector.py file and executes the
        # getDailyData() function
        data = db.getDailyData()
        for entries in data:

            # The fourth index of the tuple returned is the employee ID
            employee_id.append(entries[4])

        if input('Do you want to continue? [y/n]: ') == 'y':

            # This dictionary will be used to store the employee ID as key and
            # prediction made by the AI as value
            employee_predictions = dict()

            # This block of code loops through each unique employee and collects their
            # temperatures in a list of the form montioned at the start and how they
            # felt each day
            for employee in employee_id:
                temperatures = list()
                feelings = list()
                for entries in data:
                    if entries[4] == employee:
                        temperatures.append([entries[2], entries[3]])
                        feelings.append(entries[5])

                # Calculating the average initial temperature and feeling that month
                # This will be used as a prediction case for the AI
                sum_ = 0
                for i,j in temperatures:
                    sum_ += i
                mean_temp = sum_/len(temperatures)
                predict_feeling = 5

                # Making prediction
                predicted_finalTemp = AI(temperatures, feelings, [[mean_temp, predict_feeling]])

                employee_predictions[employee] = predicted_finalTemp[0]

            if input('Do you want to enter the predictions in the database? [y/n]: ') == 'y':

                month_year = input('Enter the date in mm_yy format: ')
                for emp_id in employee_predictions:
                    db.inputReport(emp_id, month_year, employee_predictions[emp_id])
                

        else:
            quit()

run()

