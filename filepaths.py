import os

# Stores any and all filepaths
currentDir= os.getcwd() 

# Where decompile apks reside
masterFolder= currentDir+"/APKTOOL/"
test= currentDir+"/APKTOOL/decompiled/"
# tfidf
location= currentDir+"/data/"  #folder containing files to read
tfidfdataframe= currentDir+'/data/tfidf/tfidfcompleteFeatureVector.csv' #file to output

# main dataframes
dataframesBenign= currentDir+'/data/benign.csv'
dataframesMalicious= currentDir+'/data/malicious.csv'
cleanedDataframe= currentDir+'/data/cleanedDataframe.csv'
completeFeatureVector = currentDir+'/data/completeFeatureVector.csv'


# combinations
combinationFile = currentDir+'/data/combinations.csv'#file to output
cleanedCombinations= currentDir+ '/data/cleanedCombinations.csv'
# xml parser
outputFile= currentDir+'/data/permissions.txt' #file to output
outputFileCSV= currentDir+'/data/permissions.csv' #file to output
appPermissionsFile = currentDir+'/data/appPermissions.csv' #file to output

#smali 
apicalls= currentDir+"/data/apiCalls.csv" #file to output
smaliParsed= currentDir+"/data/smaliParsed.txt"


#-------- Seperate files for when we are testing our SVM on outside apps --------

# xml parser
outputFileSample= currentDir+'/data/sample_permissions.txt' #file to output
outputFileCSVSample = currentDir+'/data/sample_permissions.csv' #file to output
appPermissionsFileSample = currentDir+'/data/sample_appPermissions.csv' #file to output

#smali 
apicallsSample= currentDir+"/data/sample_apiCalls.csv" #file to output
smaliParsedSample= currentDir+"/data/sample_smaliParsed.txt"

#Classifing with SVM
newApp = currentDir+'/data/newAppFile.csv' #This will replace the master file when decompling outside apps for testing
finalNewApp = currentDir + '/data/finalNewApp.csv'#This will hold the cross referenced features with the training dataset

# combinations
combinationFileSample = currentDir+'/data/sample_combinations.csv'#file to output