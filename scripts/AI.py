''' 

This is the Official Covidality AI code.

Please Use the Following Format for Inputting Data:

temp_final: [[t1i, t1f], [t2i, t2f], ...]
howBadDoYouFeel: List of integers from 1-10
predict_case: [initial temperature, howBadAreYouFeeling]

'''

# The main library for the AI
from sklearn import tree

def AI(temp_list, howBadDoYouFeel, predict_case):

    # Initialising some variables
    init_templist = list()
    final_templist = list()

    trainX = list()
    trainY = list()

    # Evaluates and returns 1 for feeling BAD(>=7) and 0 for feeling FINE
    def evaluateFeel(howBadDoYouFeel):

        if howBadDoYouFeel>=7:
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
        AI(features, labels, predict_this)

        print(True)
    except:

        raise ReferenceError

'''

Below is the useage of the function.

The code below has no meaning whatsoever and has been put there for the sole purpose of showing the
format of the input to be given.

Please DO NOT uncomment to code below as it serves no purpose and might act as hinderence to the 
working of the script

'''
'''
# Initial Temperature, Final Temperature
features = [[1, 2], [2, 9], [3, 5], [5, 6]]

# How Bad are you Feeling?
labels = [9, 5, 4, 11]

# Here 2 is the initial temperature and 10 is how bad you are feeling
predict_this = [[1, 6]]

# Initial Temperature, Feeling ELement
print(AI(features, labels, predict_this))
'''

