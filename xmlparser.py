import pandas as pd
from bs4 import BeautifulSoup as Soup
import regex as re
import filepaths

outputFile= filepaths.outputFile
outputFileCSV= filepaths.outputFileCSV
appPermissionsFile = filepaths.appPermissionsFile

featureVector = pd.DataFrame()


# content = []
#app name and permissions

def readXML(f):
  # Read the XML file
  with  open(f, "r", errors="ignore") as file:
      # Read each line in the file, readlines() returns a list of lines
      content = file.readlines()
      # Combine the lines in the list into a string
      content = "".join(content)
      Soup_content = Soup(content, "xml")
  return Soup_content

def ouputText(f):
  output = open(outputFile, 'w')
 
  print(f, file = output)

def getPermissionText():
  #parses the txt file and puts all permissions in a list
  pattern = re.compile("(?<=\")(.*?)(?=\")")
  f = open(outputFile)
  permissions = f.read()
  #splits permissions that are separated by ,
  listOfPermissionsText = permissions.split(",")
  listOfPermissions = []
  for i in range(len(listOfPermissionsText)):
    #puts all permissions in a list
    permissionText = re.findall(pattern,listOfPermissionsText[i])
    if permissionText:
      permission = permissionText[0]
      listOfPermissions.append(permission)
  return(listOfPermissions)

def getAppPermissions(appPermissions,parentFolder,malicious):
  #groups apps and their permissions together

  #get app name from the name of the folder
  pattern = re.compile("[^/]+$")
  
  #uses a regex to get name from parent folder name
  nameResult = re.findall(pattern, parentFolder)
  name = nameResult[0]

  if malicious == True:
    featureVector.loc[name,'malicious'] = 1
  elif malicious == False:
    featureVector.loc[name,'malicious'] = 0

  for permission in appPermissions:

    #adds permissions that are not in the feature vector
    if permission not in featureVector.columns.values:
      featureVector.loc[name, permission] = 1
  
  #cross refrences master permission set with permission set of the current app
  for feature in featureVector.columns.values:
    if feature != 'malicious':
      if feature in appPermissions:
        featureVector.loc[name,feature] = 1
      else: 
        featureVector.loc[name,feature] = 0
          
  nonZeroFV = featureVector.fillna(0)
  return nonZeroFV
  
def ouputCSV():
  featureVector.index.names=['name']
  featureVector.to_csv(appPermissionsFile, na_rep=0, header=featureVector.columns)

  
def showData(csv):
  dataframe=pd.DataFrame()
  
  return csv.head(5)


def getPermissions(Soup_content):
  result = Soup_content.find_all("uses-permission")
  return result


def parseXML(file, parentFolder,malicious):
   Soup_content= readXML(file)
   permissionlist= getPermissions(Soup_content)
   permissionsText = ouputText(set(permissionlist))
   
  #  convert file to csv process

   permissions = getPermissionText()
   fv = getAppPermissions(permissions, parentFolder,malicious)
  #  ouputCSV()