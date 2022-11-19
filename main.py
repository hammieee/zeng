from randomForestClassifier import *
from NaiveBayes import *
from supportVector import *
from integrateDataset import *
from prepDataframe import *
from generateDashboard import *
import webbrowser

'''
1. To run the program: python3 main.py
2. Enter Log file to predict percentage of ransomware
3. Dashboard will pop out after execution of main.py
'''

def main():

    #get input file
    inputLogs = input("Enter Log file of interest:")
    # Initialize the dataframe from the integrated dataset
    # returns out.csv
    combined_logs = integrateDataset()

    #manual detect
    actual_result = manualDetect(inputLogs)

    print(actual_result)

    # returns features and labels
    features, labels = getFeaturesLabels(combined_logs)
    features1, labels1 = getFeaturesLabels(inputLogs)

    # Return Format <dict>,string:
    rf_result, rf_time, rf_predict = randomForestClassifier(features, labels, features1)

    nb_result, nb_time, nb_predict = NaiveBayes(features, labels, features1)
    svc_result, svc_time, svc_predict = supportVector(features, labels, features1)

    # Add to the list below:
    # Position [rf , nb, svc]
    Accuracy_list = [list(rf_result.values())[0], list(nb_result.values())[0], list(svc_result.values())[0]]
    Precision_list = [list(rf_result.values())[1], list(nb_result.values())[1], list(svc_result.values())[1]]
    Sensitivity_list = [list(rf_result.values())[2], list(nb_result.values())[2], list(svc_result.values())[2]]
    Specificity_list = [list(rf_result.values())[3], list(nb_result.values())[3], list(svc_result.values())[3]]
    F1_score_list = [list(rf_result.values())[4], list(nb_result.values())[4], list(svc_result.values())[4]]
    time_list = [rf_time, nb_time, svc_time]
    predict_list = [actual_result,rf_predict, nb_predict, svc_predict]

    plotting_list = [Accuracy_list, Precision_list, Sensitivity_list, Specificity_list, F1_score_list, time_list]

    print(Accuracy_list,Precision_list,Sensitivity_list,Specificity_list,F1_score_list,time_list)

    # Plot the graphs
    plotGraph(plotting_list)

    # plot actual vs predicted graph
    plotActualGraph(predict_list,inputLogs)

    # Generate Dashboard
    generateDashboard()

    webbrowser.open_new_tab('index.html')


if __name__ == "__main__":
    main()


