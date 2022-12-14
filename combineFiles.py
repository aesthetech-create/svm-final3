
import pandas as pd
import filepaths
import numpy as np

# def main(fileLabel):


#   permData = pd.read_csv(filepaths.appPermissionsFile)
#   apiData = pd.read_csv(filepaths.apicalls)
  
#   combinedData = pd.merge(permData,apiData,how = 'right',on = ['name'])
#   combinedData = combinedData.set_index('name')
  
#   if fileLabel == True:
#     combinedData.to_csv(filepaths.dataframesMalicious,na_rep = 0,header=combinedData.columns)
#   elif fileLabel == False:
#     combinedData.to_csv(filepaths.dataframesBenign,na_rep = 0,header=combinedData.columns)

def main(fileLabel):
  permData = pd.read_csv(filepaths.appPermissionsFile)
  permData = permData.set_index('name')
  
  if fileLabel == True:
    permData.to_csv(filepaths.dataframesMalicious,na_rep = 0,header=permData.columns)
  elif fileLabel == False:
    permData.to_csv(filepaths.dataframesBenign,na_rep = 0,header=permData.columns)

def CreateMasterFV():
  benignDF = pd.read_csv(filepaths.dataframesBenign)
  benignDF = benignDF.set_index('name')
  maliciousDF = pd.read_csv(filepaths.dataframesMalicious)
  maliciousDF = maliciousDF.set_index('name')
  
  benignColumns = benignDF.columns.values
  maliciousColumns = maliciousDF.columns.values
  allColumns = benignColumns

  for i in range(len(maliciousColumns)):
    if maliciousColumns[i] not in allColumns:
      allColumns = np.insert(allColumns, obj = len(allColumns),values = maliciousColumns[i])

  masterFV = pd.DataFrame(columns = allColumns)

  masterFV = masterFV.append(benignDF)
  masterFV = masterFV.append(maliciousDF)
  masterFV = masterFV.set_index('name')
  #masterFV = pd.merge(benignDF,maliciousDF)
  masterFV.to_csv(filepaths.completeFeatureVector,na_rep = 0,header=masterFV.columns)
 
def sample(fileLabel):


  permData = pd.read_csv(filepaths.appPermissionsFileSample)
  #apiData = pd.read_csv(filepaths.apicallsSample)
  
  #combinedData = pd.merge(permData,apiData,how = 'right',on = ['name'])
  permData = permData.set_index('name')
  
  permData.to_csv(filepaths.newApp, na_rep= 0)