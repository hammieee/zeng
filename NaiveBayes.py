from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from comparisonResults import *

'''
1. NaiveBayes() instantiates GaussianNB to
to train the model and predict if log file 
contains ransomware
2. Returns confusion matrix results and predicted value
'''

def NaiveBayes(features,labels, inputLogs):
    model_name = "NaiveBayes"
    # Grab Currrent Time Before Running the Code
    start = time.time()
    cal_fact2(2500)

    # split X and y into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.8, random_state = 42)
    # train a Gaussian Naive Bayes classifier on the training set
    # instantiate the model
    gnb = GaussianNB()

    # fit the model
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)

    # Grab Current Time After Running the Code
    end = time.time()

    #Subtract Start Time from The End Time
    total_time = end - start
    #print("\n"+ str(total_time))

    #Learning curve function
    learningCurve(X_train, y_train,model_name)

    #Confusion matrix
    confusion_matrix = confusionMatrix(y_test, y_pred,model_name)

    # predict logs
    log_prediction = gnb.predict(inputLogs)

    Truecount = 0
    for i in log_prediction:
        if i == True:
            Truecount += 1

    ransomware_percentage = Truecount / len(log_prediction)

    return confusion_matrix,total_time, ransomware_percentage





