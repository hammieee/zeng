# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Import the model we are using
from sklearn.ensemble import RandomForestClassifier

from comparisonResults import *

'''
1. randomForestClassifier() instantiates RandomForestClassifier to
to train the model and predict if log file 
contains ransomware
2. Returns confusion matrix results and predicted value
'''
def randomForestClassifier(features, labels,inputLogs):
    model_name = "RandomForest"
    # Grab Currrent Time Before Running the Code
    start = time.time()
    cal_fact2(2500)
    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size =0.8, random_state = 42)

    # Instantiate model with 1000 decision trees
    clf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
    # Train the model on training data
    clf.fit(train_features, train_labels);

    # performing predictions on the test dataset
    y_pred = clf.predict(test_features)

    # Grab Currrent Time After Running the Code
    end = time.time()
    # Subtract Start Time from The End Time
    total_time = end - start

    #Learning curve function
    learningCurve(train_features, train_labels, model_name)

    # Confusion matriz
    confusion_matrix = confusionMatrix(test_labels, y_pred, model_name)

    # predict logs
    log_prediction = clf.predict(inputLogs)
    Truecount = 0
    for i in log_prediction:
        if i == True:
            Truecount += 1

    ransomware_percentage = Truecount / len(log_prediction)

    return confusion_matrix, total_time, ransomware_percentage


