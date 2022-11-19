# metrics are used to find accuracy or error
from sklearn import metrics
import scikitplot as skplt
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

'''
1. Calculates time taken for model to train
'''
def cal_fact2(n):
    if n == 1:
        return n
    else:
        result = 1
        for i in range(2,n+1):
            result = result * i
        return result

'''
1. Plots ransomware classification learning curve
2. saved in images folder
'''
def learningCurve(train_features,train_labels, model_name):
    # Learning curve
    skplt.estimators.plot_learning_curve(RandomForestClassifier(), train_features, train_labels,
                                         cv=7, shuffle=True, scoring="accuracy",
                                         n_jobs=-1, figsize=(6, 4), title_fontsize="large", text_fontsize="large",
                                         title="Ransomware Classification Learning Curve ("+model_name+")");
    plt.savefig('images/'+model_name+'_learning_curve.png',bbox_inches='tight')

'''
1. Plots Confusion matrix graph
2. saved in images folder
'''
def confusionMatrix(test_labels, y_pred,model_name):
    confusion_matrix = metrics.confusion_matrix(test_labels, y_pred)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,
                                                display_labels=["Not Ransomware", "Ransomware"])
    cm_display.plot()
    cm_display.ax_.set_title("Confusion Matrix ("+model_name+")")
    plt.savefig('images/'+model_name+'_matrix.png', bbox_inches='tight')

    # using metrics module for accuracy, precision, sensitivity recall, Specificity, F1_score calculation
    Accuracy = metrics.accuracy_score(test_labels, y_pred)
    Precision = metrics.precision_score(test_labels, y_pred)
    Sensitivity_recall = metrics.recall_score(test_labels, y_pred)
    Specificity = metrics.recall_score(test_labels, y_pred, pos_label=0)
    F1_score = metrics.f1_score(test_labels, y_pred)

    # metrics
    return({"Accuracy": Accuracy, "Precision": Precision, "Sensitivity_recall": Sensitivity_recall,
           "Specificity": Specificity, "F1_score": F1_score})

'''
1. Plots created metrics graph
2. saved in images folder
'''
def plotGraph(plotting_list):
    count =0
    x = ["Random Forest", "Naive Bayes", "Support Vector"]

    for list in plotting_list:
        filename = "images/"+str(count)+".png"
        y = list
        plt.clf()
        if count==0:
            plt.title("Accuracy")
        elif count ==1:
            plt.title("Precision")
        elif count ==2:
            plt.title("Sensitivity")
        elif count ==3:
            plt.title("Specificity")
        elif count ==4:
            plt.title("F1 Score")
        elif count ==5:
            plt.title("Time Taken")
        barlist= plt.bar(x, y)
        barlist[0].set_color('b')
        barlist[1].set_color('g')
        plt.savefig(filename)
        count+=1

'''
1. Plots actual vs predicted graph
2. saved in images folder
'''
def plotActualGraph(predict_list, inputLogs):
    x = ["Actual","Random Forest", "Naive Bayes", "Support Vector"]
    y = predict_list
    plt.clf()
    plt.title("Percentage of ransomware detected (" +inputLogs+")")
    barlist = plt.bar(x, y)
    barlist[0].set_color('r')
    barlist[1].set_color('b')
    barlist[2].set_color('g')
    plt.savefig("images/actual.png")