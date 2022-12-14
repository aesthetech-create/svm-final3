import smaliparserSample
import xmlparserSample
import combineFiles
import newapp
import combinationsSample

    # find current folder


import os
import filepaths

# set where decompiled apks are from filepaths
   
masterFolder= filepaths.masterFolder
list_of_apps = os.listdir(masterFolder)

pathList=[]
fileLabel= False

def main():
    global fileLabel
    fileLabel= False  #CHANGE HERE  false== begign, true== malicous
    i = 0
    for root, dirs, files in os.walk(masterFolder):
            
            
            
        for file in files:
                # get app name from root folder
                filePath= os.path.join(root, file)
                if ('original' in root):
                    continue

                if ('unknown' in root):
                    continue

                if file.endswith("AndroidManifest.xml") :
                    i += 1  
                    #call xml parser here ()
                    print("Counter: " , i, "File path: " + filePath)
                    xmlparserSample.parseXML(filePath, filePath,fileLabel)
             
                
                # if file.endswith(".smali"):
                #     #call smali parse here
                #     smaliparserSample.runsmaliParser(fileLabel, filePath)
                

        
    # get smali dataframe
    # smaliparserSample.getFinalDataFile()
    # get xml dataframe
    xmlparserSample.ouputCSV()
    # outputs csv with all features, for either begign or malicious apps
    combineFiles.sample(fileLabel)
    
    #This is a line that you will run when getting features for an outside app that is not in the dataset
    
    newapp.createNewApp(filepaths.completeFeatureVector, filepaths.newApp, filepaths.finalNewApp)
    combinationsSample.combo2()
    

main()


    


