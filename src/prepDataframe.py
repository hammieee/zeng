import pandas as pd
import pathlib
import os
import requests
from sklearn import preprocessing
import numpy as np

'''
1. getOfficialExtensions() gets an existing list of
recognised extension from the team's github
2. Returns an array of recognised extensions
'''
def getOfficialExtensions():
    # Get Official extension text file from github
    extension_url = "https://raw.githubusercontent.com/hammieee/zeng/main/extensions.txt"
    req = requests.get(extension_url)
    req = req.text

    # Write into extensions local txt file
    f = open("extensions.txt", "w")
    f.write(req)
    f.close()

    # Read extensions.txt as array using readlines()
    file1 = open('extensions.txt', 'r')
    Lines = file1.readlines()

    # Official extensions list
    file_ext_list = []
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        file_ext_list.append(line)

    return file_ext_list

'''
1. prepData() uses the csv data to extract file extensions
from process.args and file.path
2. If extracted file extension contains shell script extension
or is unrecognised, it will be labelled as ransomware
3. Returns dataframe with columns: ShellExtension, FilepathExtension, RansomwareResult
'''
def prepData(combined_logs):
    integrated_df = pd.read_csv(combined_logs)

    # Initialize dataframe
    df = pd.DataFrame(
        {
            "ProcessArgs": [],
            "FileExt": [],
        }
    )

    # Add process.args and file.path to df dataframe
    df['ProcessArgs'] = integrated_df['process.args']
    df['FileExt'] = integrated_df['file.path']

    # Convert ProcessArgs ad filepath dataframe to list
    process_list = df['ProcessArgs'].tolist()
    filepath_list = df['FileExt'].tolist()

    # get official extensions list from github
    file_ext_list = getOfficialExtensions()

    # List of shell script extensions
    shell_script_list = [".sh", ".py", ".ps1", ".psm1"]

    # Extracted file extensions will be appended
    foundShellExtension = []
    foundSusExtensions = []

    # True false values will be appended
    Ransomware_result_list = []

    for i in range(len(df)):
        process_list_strings = str(process_list[i]).split(", ")
        filename = os.path.basename(str(filepath_list[i]))

        # create list of found file extensions
        string = ""
        for x in process_list_strings:
            if "." in x:
                filename = os.path.basename(x)
                file_extension = pathlib.Path(filename).suffix
                string += file_extension + " "
        # append string to foundShellExtension
        foundShellExtension.append(string)

        # If process arg contains shell script extension
        res1 = any(ele in str(process_list[i]) for ele in shell_script_list)
        res2 = any(ele in filename for ele in shell_script_list)

        if "." in filename:
            # function to return the file extension
            file_extension = pathlib.Path(filename).suffix
            foundSusExtensions.append(file_extension)

            # If file extension is not found in official extension list
            if file_extension not in file_ext_list:
                Ransomware_result_list.append(True)
            else:
                Ransomware_result_list.append(False)
        elif res1 == True or res2 == True:
            Ransomware_result_list.append(True)
        else:
            Ransomware_result_list.append(False)
            foundSusExtensions.append("")

    # inserting new column with values of list made above
    df.insert(2, "ShellExtension", foundShellExtension)
    df.insert(3, "FilePathExtensions", foundSusExtensions)
    df.insert(3, "RansomwareResult", Ransomware_result_list)

    return df


'''
1. getFeaturesLabels() preprocesses the dataframe
2. Dataframe is encoded using LabelEncoder()
3. Returns features: ShellExtension,FilePathExtensions
4. Returns labels: RansomwareResult
'''
def getFeaturesLabels(combined_logs):
    features = prepData(combined_logs)

    # Prep Training Dataset
    # Features: Only need FilePathExtensions, ShellExtension
    # Label: RansomwareResult

    # Encode the data
    le = preprocessing.LabelEncoder()
    for column_name in features.columns:
     if features[column_name].dtype == object:
       features[column_name] = le.fit_transform(features[column_name])
     else:
       pass

    # Separate into Features and Label and convert to numpy array
    labels = np.array(features['RansomwareResult'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    features= features.drop('RansomwareResult', axis = 1)
    features= features.drop('ProcessArgs', axis = 1)
    features= features.drop('FileExt', axis = 1)

    # Convert to numpy array
    features = np.array(features)

    return features,labels

'''
1. manualDetect() calculates the percentage of
ransomware detected in the log file of interest
2. Used as actual result to compare with predicted results
3. Returns percentage of ransomware detected
'''
def manualDetect(combined_logs):
    df = prepData(combined_logs)
    Ransomware_result_list = df['RansomwareResult'].tolist()

    Truecount=0
    for i in Ransomware_result_list:
        if i == True:
            Truecount += 1
    ransomware_percentage = Truecount / len(Ransomware_result_list)
    return ransomware_percentage
