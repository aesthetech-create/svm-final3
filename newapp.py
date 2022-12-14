import pandas as pd
import numpy as np
import filepaths
#This will run when we want to create a csv to test our SVM on 

def createNewApp(trainingFile, newAppFile, finalNewApp):
  training = pd.read_csv(trainingFile)
  training = training.set_index('name')

  newApp = pd.read_csv(newAppFile)
  newApp = newApp.set_index('name')
  #This should work for combinations but this will have to take place after combinations happen
  finalColumns = training.columns.values
  for column in newApp.columns.values:
    if column not in finalColumns:
      newApp.pop(column)
  for column in finalColumns:
    if column not in newApp.columns.values:
      newApp[column] = 0
  newApp.pop('malicious')#removes class label for unknown app


  print(newApp.columns.values)
  newApp.to_csv(finalNewApp, na_rep = 0)

