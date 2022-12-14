import pandas as pd
import numpy as np
import filepaths

#completeFeatureVector = filepaths.completeFeatureVector
cleanedDataframe= filepaths.finalNewApp
combinationFile = filepaths.combinationFileSample
#removes features that are not very common to begin with
#If a feature is not common, then all possible combinations containing that feature will be uncommon

#need to find a minimum support for a each to make it into the combinations

# def removeMonotone(features,featureVector):
#   counts = [None] *len(features) #holds the number of times a feature with the corresponding index in the column list
#   rows = featureVector.shape[0] #counts the number of rows in feature vector, this is the highest possible frequency of an item
#   for feature in range(len(features)):
#     fs = sum(featureVector[features[feature]])
#     counts[feature] = fs

#   #calculates the support of each column
#   for i in range(len(counts)):
#     counts[i] = counts[i]/rows
#   minsup = 0

#   nonMonotoneColumns = []

#   for i in range(len(counts)):
#     if counts[i] > minsup:
#       nonMonotoneColumns.append(features[i])
#   return nonMonotoneColumns
  
  


def create2Combinations(featureVector):
  columns = featureVector.columns.values
  features = columns[1:]
  #nonMonotoneColumns = removeMonotone(features, featureVector)
  combinationColumns = []
  combinationFeatureVector = pd.DataFrame()

  # for i in range(len(features)-1):
  #   for j in range(i+1,len(features)):
  #     print(i,j)
  #     combinationFeatureVector[features[i],features[j]] = 0

  #If the app has both of the values in the set, the value of the key value pair is 1
  #adding apps that have the specific sets of feature combinations
  # apps = featureVector['name']#names of the apps

  
  # numOfApps = 0
  # for app in apps: 
  #   appData = {'name': app}
  #   for i in range(len(combinationFeatureVector.columns.values)):
  #     combinations = combinationFeatureVector.columns.values

  #     currentCombination = combinations[i]
  #     currentRow = featureVector.iloc[numOfApps]
  #     if(currentCombination != 'name'):
  #       if (currentRow[currentCombination[0]] == 1) & (currentRow[currentCombination[1]] == 1):
  #         str1 = str(currentCombination[0])
  #         str2 =  str(currentCombination[1])
  #         finalstr = str1,str2
  #         appData[finalstr] = 1
  #       else:
  #         str1 = str(currentCombination[0])
  #         str2 =  str(currentCombination[1])
  #         finalstr = str1,str2
  #         appData[finalstr] = 0
  #   df = pd.DataFrame(appData, index = [appData["name"]])
  #   df = df.set_index('name')
  #   combinationFeatureVector = combinationFeatureVector.append(df)
  #   numOfApps += 1

  # combinationFeatureVector.index.name = 'name'
  # featureVector = featureVector.set_index('name')
  # featureVector.index.name = 'name'
  
  training = pd.read_csv(filepaths.combinationFile)
  testing = pd.read_csv(filepaths.finalNewApp)
  training = training.set_index('name')
  testing = testing.set_index('name')
  temp = pd.DataFrame(columns=training.columns.values)
  columns = training.columns.values
  apps = list(testing.index.values)
  # 1. test if the column exists
  #
  for app in apps:
    approw = {'name': app}
    for col in columns[1:]:
      og_column = col[1:-1]
      col_data = og_column.split(",")
      col_data_first = col_data[0][1:-1]
      col_data_second = col_data[1][2:-1]
      try:
        if testing.loc[app, col_data_first] == 1 and testing.loc[app, col_data_second] == 1:
          approw[col] = 1
      except:
        approw[col] = 0
    temp = temp.append(approw, ignore_index = True)
#   combinationFeatureVector['malicious'] = ''
#   for ind in combinationFeatureVector.index:
#     combinationFeatureVector.loc[ind,'malicious'] = featureVector.loc[ind,'malicious']
  
#   malicious= combinationFeatureVector.pop('malicious')
#   combinationFeatureVector.insert(0,'malicious', malicious)
  nonZeroFV = temp.fillna(0)
  nonZeroFV.pop(temp.columns.values[0])
  nonZeroFV = nonZeroFV.set_index('name')
  nonZeroFV.to_csv(filepaths.combinationFileSample)

def create3Combinations(featureVector):
  columns = featureVector.columns.values
  features = columns[1:]
  #nonMonotoneColumns = removeMonotone(features, featureVector)
  combinationColumns = []
  combinationFeatureVector = pd.DataFrame()

  for i in range(len(features)-1):
    for j in range(i+1,len(features)):
        for k in range(j+1, len(features)):
            combinationFeatureVector[features[i],features[j],features[k]] = 0

  #If the app has both of the values in the set, the value of the key value pair is 1
  #adding apps that have the specific sets of feature combinations
  apps = featureVector['name']#names of the apps

  
  numOfApps = 0
  for app in apps: 
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

#   combinationFeatureVector['malicious'] = ''
#   for ind in combinationFeatureVector.index:
#     combinationFeatureVector.loc[ind,'malicious'] = featureVector.loc[ind,'malicious']
  
#   malicious= combinationFeatureVector.pop('malicious')
#   combinationFeatureVector.insert(0,'malicious', malicious)
  nonZeroFV = combinationFeatureVector.fillna(0)
  
  nonZeroFV.to_csv(combinationFile)

def combo2():
    print("Combinations Running")
    featureVector = pd.read_csv(filepaths.completeFeatureVector)
    create2Combinations(featureVector)

