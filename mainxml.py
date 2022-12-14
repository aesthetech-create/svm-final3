import smaliparser
import xmlparser
import combineFiles
import newapp

# find current folder

import os
import filepaths

# set where decompiled apks are from filepaths
   
masterFolder= filepaths.masterFolder
list_of_apps = os.listdir(masterFolder)

pathList=[]
fileLabel= False  #Not the one that needs to change

def main():
    global fileLabel
    fileLabel= False  #CHANGE HERE  false== begign, true== malicous
    dir = 0
    filecount = 0
    
    for root, dirs, files in os.walk(masterFolder):
        # if dir > 250:
        #     break
        dir += 1
        filecount += 1 
        for file in files:
                # get app name from root folder
                filePath= os.path.join(root, file)
                if ('original' in root):
                    filecount += 1
                    continue

                if ('unknown' in root):
                    filecount += 1
                    continue

                if file.endswith("AndroidManifest.xml") :  
                    #call xml parser here ()
                    print("DIR NUMBER: ", dir, " | FILE NUMBER: ", filecount, " | XML    | FILE PATH: ", filePath)
                    filecount += 1
                    xmlparser.parseXML(filePath, filePath,fileLabel)
             
                if file.endswith(".smali"):
                    filecount += 1
                

        
    # get smali dataframe
    # smaliparser.getFinalDataFile()
    # get xml dataframe
    xmlparser.ouputCSV()
    combineFiles.main(fileLabel) # outputs csv with all features, for either begign or malicious apps
    
    
    #This is a line that you will run when getting features for an outside app that is not in the dataset
    #You will have to change the file directory where the master file is saved so the trainingset master file is preserved
    #The new master file must be set to filepaths.newApp for this to work
    
    #newapp.createNewApp(filepaths.cleanedDataframe, filepaths.newApp, filepaths.finalNewApp)
    

main()


    


