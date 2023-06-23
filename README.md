# svm-final3
Our Senior Project at NYIT: building a simple SVM that takes Android API calls and app permissions to detect if an Android app is malicious.
This took data from the [MalDroid-2020](http://205.174.165.80/CICDataset/MalDroid-2020/Dataset/CSV/) (will require a .edu email) dataset, consisting of thousands of applications. 

# Data
About 20 000 apps, 10 000  benign and 10 000 malicious, were used for the SVM. They were randomly selected on Python. About 9900 of each were used instead; some apps had non-traditional manifest files and therefore could not be processed by our parser. (this is often files like non-Latin manifests, or sub-libraries that had their own manifest files.)
The apps were decompiled using APKTOOL, a .jar application that was used to decompile .apk files into the data files that we need. It also provides a useful object abstraction that we can use for processing.

# Process
These decompiled files are then searched to get relevant files like .smali and .manifest files, and their data is extracted using regex on Python.
We then create a numpy dataframe and create binary flags where aforementioned permissions exist as the rows, and store them as records in the dataframe.
They then serve as values to be put into the SVM.
