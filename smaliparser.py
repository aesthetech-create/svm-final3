
import filepaths
import pandas as pd
import re

import smali
from smali import SmaliFile

import asyncio

commonAPIs = ['getDeviceId()','getSubscriberId()','execHttpRequest()'
             'setWifiEnabled()','sendTextMessage()', 'Runtime.exec()'
             , 'Cipher.getInstance()','Ljavac/sql/ConnectionEvent;.<init>:(Ljavax/sql/PooledConnection;Ljava/sql/SQLException;)V'
             ,'Ljava/nio/channels/WriteableByteChannel;close:()V'
             ,'Landroid/service/carrier/CarrierService;.stopSelf:()V'
             , 'Landroid/app/NativeActivity;.getVolumerControlStream:()I'
             , 'Landroid/widget/AdapterView;.refreshDrawableState:()V'
             , 'Landroid/opengl/Matrix;.getClass:()Ljava/lang/Class;'
             , 'Landroid/widget/MultiAutoCompleteTextView;.saveHierarchyState:(Landroid/util/SparseArray;)V'
             , 'Landroid/view/ViewStructure;.setCheckable:(Z)V'
             , 'Landroid/text/method/BaseKeyListener;.getInputType:()I'
             , 'Landroid/provider/MediaStore$Images$Media;.wait:(J)V'
             , 'Ljava/lang/Object;.<init>:()V', 'Ljava/lang/StringBuilder;.toString:()Ljava/lang/String;'
             , 'Ljava/lang/StringBuilder;.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'Landroid/app/Activity;.<init>:()V'
             , 'Ljava/lang/StringBuilder;.<init>:()V' , 'Ljava/lang/String;.equals:(Ljava/lang/Object;)Z'
             , 'Ljava/lang/StringBuilder;.append:(I)Ljava/lang/StringBuilder;'
             , 'Ljava/util/ArrayList;.<init>:()V', 'Ljava/util/Iterator;.hasNext:()Z'
             , 'Ljava/util/Iterator;.next:()Ljava/lang/Object;''Landroid/content/BroadcastReceiver;.<init>:()V'
             , 'Landroid/content/Context;.getSystemService:(Ljava/lang/String;)Ljava/lang/Object;'
             , 'Landroid/content/Intent;.<init>:(Landroid/content/Context;Ljava/lang/Class;)V'
             , 'Landroid/net/Uri;.parse:(Ljava/lang/String;)Landroid/net/Uri;']

outputFile= filepaths.smaliParsed
# create dataframe
firstColumnName= "APP" #Name the very first column- it will hold document or item row names, new rows will be added based on this column len(index)
corpusDF= pd.DataFrame(columns=[firstColumnName]) #create dataframe with the column, rows to be added later with token columns and values
label=[]
global previousFilePath
previousFilePath=" "
index=0 #keep track of current row index, increment with new row in checkAddIndexRow

def parseToFieldAndData(file):
    parse_lines = file.lines
    fieldAndData = []
    for line in parse_lines:
      # check and add here for malicious api calls
      if line in commonAPIs:
        fieldAndData.append(line)
      methodsList = re.findall('\->.+', line)
        # check and add here again for api calls
      truecount = 0
      if (methodsList != []): 
#         if (methodsList[0] != '->writeInt(I)V'):
          if(methodsList[0][2:] in commonAPIs or methodsList[0] in commonAPIs):
              fieldAndData.append(methodsList[0][2:])
              truecount += 1
              print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HEY THE TRUE COUNT WENT UP!!!!!!! COUNT IS: " + truecount)
    return fieldAndData



# Check if row exist, add new rows, return current row index (row= docName or item in the firstColumn)
# if its the very first row add at 0 and current index=0
# if row doesnt exist add row at len(df.index)/the end of the df and save current index=df.index
# if row exists just return current index (value should stay the same from past conditions until new row/doc changes it)
def checkAddIndexRow(rowName):
  index=0
  # check if dataframe is empty
  if corpusDF.empty:
    # if empty add new from 0
    corpusDF.loc[0] = [rowName]
    index=0
  else:
    # check if row name exists 
    if ((rowName in corpusDF[firstColumnName].values) != True):
      index= len(corpusDF.index)
      corpusDF.loc[index,[firstColumnName]] = [rowName]
    else:
      # get index of row
      index=len(corpusDF.index)-1
      
      
  return index
  
# get doc/item name, and tokens list
# use checkAddIndexRow() to get current row index (more info on checkAddIndexRow above the function)
# loop through tokens list to get token
# get token count from tokens list, set value for current doc row and token column
# remove token from tokens list to reduce remaining time from duplicate tokens
def addtoDF(rowName,tokensList):
  index= checkAddIndexRow(rowName)
  for tokens in tokensList:
    # Count tokens in tokens list and set value
    corpusDF.loc[index,[tokens]]= 1
    tokensList.remove(tokens)
    
def ouputText(f):
  print("output text working?")
  output = open(outputFile, 'w')
 
  print(f, file= output)

def getText():
  f = open(outputFile)
  calls = f.read()
  #splits permissions that are separated by ,
  listOfText = calls.split(",")
  return listOfText

def getLabel(appName,l):
  global previousFilePath
  
  if previousFilePath != appName:
    previousFilePath= appName
    if l== True:
      label.append(1)
    elif l ==False:
      label.append(0)
    else:
      label.append(-1)

def main(fileName, path):
    parse_data = SmaliFile.parse_file(path)
    parsed=parseToFieldAndData(parse_data)

    # Add data to dataframe
    addtoDF(fileName,parsed)


def showDataframe(numOfRows):
    return corpusDF.head(numOfRows)

def getFinalDataFile():
    corpusDFinal=corpusDF
    corpusDFinal
    corpusDFinal = corpusDF.set_index(firstColumnName) #make app column index
    corpusDFinal.index.names = ["name"] #make index name null
    
    # corpusDFinal=corpusDF.rename(columns = {firstColumnName:None})  
   
    corpusDFinal.to_csv(filepaths.apicalls, na_rep=0, header=corpusDFinal.columns) #output csvFile

def runsmaliParser(fileLabel, filePath):
    # print('smali parser running')
    #get app name from the name of the folder
    pattern = re.compile("[^/]+$")

    #uses a regex to get name from parent folder name
    nameResult = re.findall(pattern, filePath)
    # print("parent folder: ",filePath)
    namefrag = nameResult[0].split("\\")
    name = namefrag[0]
    main(name, filePath)
    


