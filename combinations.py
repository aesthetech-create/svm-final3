import pandas as pd
import numpy as np
import filepaths

completeFeatureVector = filepaths.completeFeatureVector
cleanedDataframe= filepaths.cleanedDataframe
combinationFile = filepaths.combinationFile
#removes features that are not very common to begin with
#If a feature is not common, then all possible combinations containing that feature will be uncommon

#need to find a minimum support for a each to make it into the combinations

def removeMonotone(features,featureVector):
  counts = [None] *len(features) #holds the number of times a feature with the corresponding index in the column list
  rows = featureVector.shape[0] #counts the number of rows in feature vector, this is the highest possible frequency of an item
  for feature in range(len(features)):
    fs = sum(featureVector[features[feature]])
    counts[feature] = fs

  #calculates the support of each column
  for i in range(len(counts)):
    counts[i] = counts[i]/rows
  minsup = 0.15

  nonMonotoneColumns = []

  for i in range(len(counts)):
    if counts[i] > minsup:
      nonMonotoneColumns.append(features[i])
  return nonMonotoneColumns
  
  


def create2Combinations(featureVector):
  columns = featureVector.columns.values
  features = columns[2:]
  nonMonotoneColumns = removeMonotone(features, featureVector)
  combinationColumns = []
  combinationFeatureVector = pd.DataFrame()

  for i in range(len(nonMonotoneColumns)-1):
    for j in range(i+1,len(nonMonotoneColumns)):
      combinationFeatureVector[nonMonotoneColumns[i],nonMonotoneColumns[j]] = 0

  #If the app has both of the values in the set, the value of the key value pair is 1
  #adding apps that have the specific sets of feature combinations
  apps = featureVector['name']#names of the apps

  
  numOfApps = 0
  for app in apps: 
    #print(app)
    appData = {'name': app}
    len(combinationFeatureVector.columns.values)
    for i in range(len(combinationFeatureVector.columns.values)):
      
      combinations = combinationFeatureVector.columns.values

      currentCombination = combinations[i]
      currentRow = featureVector.iloc[numOfApps]
      if(currentCombination != 'name'):
        if (currentRow[currentCombination[0]] == 1) & (currentRow[currentCombination[1]] == 1):
          str1 = str(currentCombination[0])
          str2 =  str(currentCombination[1])
          finalstr = str1,str2
          appData[finalstr] = 1.0
        else:
          str1 = str(currentCombination[0])
          str2 =  str(currentCombination[1])
          finalstr = str1,str2
          appData[finalstr] = 0.0
    df = pd.DataFrame(appData, index = [appData["name"]])
    df = df.set_index('name')
    combinationFeatureVector = combinationFeatureVector.append(df)
    numOfApps += 1
    print(numOfApps)

  combinationFeatureVector.index.name = 'name'
  featureVector = featureVector.set_index('name')
  featureVector.index.name = 'name'

  combinationFeatureVector['malicious'] = ''
  for ind in combinationFeatureVector.index:
    combinationFeatureVector.loc[ind,'malicious'] = featureVector.loc[ind,'malicious']
  
  malicious= combinationFeatureVector.pop('malicious')
  combinationFeatureVector.insert(0,'malicious', malicious)
  nonZeroFV = combinationFeatureVector.fillna(0)
  
  nonZeroFV.to_csv(combinationFile)

def create3Combinations(featureVector):
  columns = featureVector.columns.values
  features = columns[2:]
  nonMonotoneColumns = removeMonotone(features, featureVector)
  combinationColumns = []
  combinationFeatureVector = pd.DataFrame()

  for i in range(len(nonMonotoneColumns)-2):
    for j in range(i+1,len(nonMonotoneColumns)-1):
      for k in range(j+1,len(nonMonotoneColumns)):
        combinationFeatureVector[nonMonotoneColumns[i],nonMonotoneColumns[j],nonMonotoneColumns[k]] = 0

  #If the app has both of the values in the set, the value of the key value pair is 1
  #adding apps that have the specific sets of feature combinations
  apps = featureVector['name']#names of the apps

  
  numOfApps = 0
  for app in apps: 
    #print(app)
    appData = {'name': app}
    for i in range(len(combinationFeatureVector.columns.values)):
      combinations = combinationFeatureVector.columns.values

      currentCombination = combinations[i]
      currentRow = featureVector.iloc[numOfApps]
      if(currentCombination != 'name'):
        if (currentRow[currentCombination[0]] == 1) & (currentRow[currentCombination[1]] == 1) & (currentRow[currentCombination[2]] == 1):
          str1 = str(currentCombination[0])
          str2 =  str(currentCombination[1])
          str3 = str(currentCombination[2])
          finalstr = str1,str2,str3
          appData[finalstr] = 1
        else:
          str1 = str(currentCombination[0])
          str2 =  str(currentCombination[1])
          str3 = str(currentCombination[2])
          finalstr = str1,str2,str3
          appData[finalstr] = 0
    df = pd.DataFrame(appData, index = [appData["name"]])
    df = df.set_index('name')
    combinationFeatureVector = combinationFeatureVector.append(df)
    numOfApps += 1

  combinationFeatureVector.index.name = 'name'
  featureVector = featureVector.set_index('name')
  featureVector.index.name = 'name'

  combinationFeatureVector['malicious'] = ''
  for ind in combinationFeatureVector.index:
    combinationFeatureVector.loc[ind,'malicious'] = featureVector.loc[ind,'malicious']

  combinationFeatureVector.to_csv(combinationFile)

def combo2():
    print("Combinations Running")
    featureVector = pd.read_csv(completeFeatureVector)
    create2Combinations(featureVector)

