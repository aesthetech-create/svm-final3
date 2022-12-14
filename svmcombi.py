from sklearn import svm
import filepaths
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump, load
from os import walk

# initial importing
datafile = open(filepaths.combinationFile)
dataset = pd.read_csv(datafile)
dataset = dataset.set_index('name')

# getting benign/malicious labels
class_label = dataset['malicious'].tolist()
classifier = svm.LinearSVC(max_iter=10000)
rows = dataset.values[:,1:]
y = class_label
x = rows
classifier.fit(x, y)

# import test data
testfile = open(filepaths.combinationFileSample)
testset = pd.read_csv(testfile)
testset = testset.set_index('name')
testfilenames = list(testset.index.values)

# do the prediction based on constructed SVM
predicted_values = classifier.predict(testset.values[:,0:])

# dictionary to store file names and their predictions for metrics
testpredict = {}
for i in range(len(testset)):
    testpredict[testfilenames[i]] = predicted_values[i]

for key in testpredict.keys():
    if testpredict[key] == 1:
        print("The file", key, "is malicious!")
    else:
        print("This file", key, "is benign!")

# # sourcing files from specific filepaths - these were given in the original dataset as benign or a type of malicious app
# truevalue = {}
# for (dirpath, dirnames, filenames) in walk("C:\\Users\\Chin Ho Kua\\Documents\\GitHub\\xda-formed\\Malignant-decom\\smsware\\test"):
#     for i in range(len(dirnames)):
#         truevalue[dirnames[i]+"\\AndroidManifest.xml"] = 1
#     break
# for (dirpath, dirnames, filenames) in walk("C:\\Users\\Chin Ho Kua\\Documents\\GitHub\\xda-formed\\Malignant-decom\\adware\\realtest"):
#     for i in range(len(dirnames)):
#         truevalue[dirnames[i]+"\\AndroidManifest.xml"] = 1
#     break
# for (dirpath, dirnames, filenames) in walk("C:\\Users\\Chin Ho Kua\\Documents\\GitHub\\xda-formed\\Malignant-decom\\riskware\\test"):
#     for i in range(len(dirnames)):
#         truevalue[dirnames[i]+"\\AndroidManifest.xml"] = 1
#     break
# for (dirpath, dirnames, filenames) in walk("C:\\Users\\Chin Ho Kua\\Documents\\GitHub\\xda-formed\\Malignant-decom\\bankingware\\test"):
#     for i in range(len(dirnames)):
#         truevalue[dirnames[i]+"\\AndroidManifest.xml"] = 1
#     break
# for (dirpath, dirnames, filenames) in walk("C:\\Users\\Chin Ho Kua\\Documents\\GitHub\\xda-formed\\benign-decom\\test"):
#     for i in range(len(dirnames)):
#         truevalue[dirnames[i]+"\\AndroidManifest.xml"] = 0
#     break


# generating metrics
# truepos = 0
# trueneg = 0
# falsepos = 0
# falseneg = 0
# print(list(set(testpredict.keys())-set(truevalue.keys())))
# for key in truevalue.keys():
#     # these four specific keys were invalid - placed in testing folder but not valid
#     # most likely because app needed no permissions declared in its manifest
#     if (key != "1ab4af024db60eefe4d1d3a11ed2d1a5\\AndroidManifest.xml" and key != "1b0e6a2c5ae70b0c7610843f39caf930\\AndroidManifest.xml" 
#         and key != "1b2cbf2a6b506542d6672a06d7d93791\\AndroidManifest.xml" and key != "1b9bb75884f1e9a9e532136960011f60\\AndroidManifest.xml"):
#         outcome = truevalue[key] - testpredict[key]
#         if outcome == 1:
#             falseneg += 1
#         elif outcome == -1:
#             falsepos += 1
#         else:
#             if truevalue[key] == 1:
#                 truepos += 1
#             else:
#                 trueneg += 1
# print("True positives:", truepos)
# print("True negatives:", trueneg)
# print("False positives:", falsepos)
# print("False negatives:", falseneg)
# print("Accuracy:", str(round((truepos+trueneg)/(truepos + trueneg + falsepos + falseneg)*100,2)) + "%")
# print("Recall:", str(round((truepos)/(truepos + falseneg)*100,2)) + "%")


# pickle svm as a file
dump(classifier, 'svm.joblib')

# graphing coefficients
plt.bar(list(testset.columns.values), classifier.coef_[0])
plt.show()
