from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from comparisonResults import *


'''
1. supportVector() instantiates SVC to
to train the model and predict if log file 
contains ransomware
2. Returns confusion matrix results and predicted value
'''
def supportVector(features, labels, inputLogs):
    model_name = "SupportVector"
    # Grab Currrent Time Before Running the Code
    start = time.time()
    cal_fact2(2500)

    # split X and y into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.8, random_state=42)
    # train a Gaussian Naive Bayes classifier on the training set
    # instantiate the model
    # Create a svm Classifier
    clf = SVC(kernel='linear')  # Linear Kernel

    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Grab Current Time After Running the Code
    end = time.time()

    # Subtract Start Time from The End Time
    total_time = end - start

    # Learning curve function
    learningCurve(X_train, y_train, model_name)

    # Confusion matrix
    confusion_matrix = confusionMatrix(y_test, y_pred,model_name)

    # predict logs
    log_prediction = clf.predict(inputLogs)
    Truecount = 0
    for i in log_prediction:
        if i == True:
            Truecount += 1

    ransomware_percentage = Truecount / len(log_prediction)

    return confusion_matrix, total_time, ransomware_percentage



