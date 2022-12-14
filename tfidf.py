import os

import numpy as np
import pandas as pd
import filepaths

location= filepaths.completeFeatureVector
combo= filepaths.combinationFile
corpus=[]
dataframes= []



# create corpus from dataframe for column values =1
def createCorpus(df):
  corpus.clear() #always clear before 
  
  appNames= df.index.values #store index val
  
  
  if 'malicious' in  df.columns.values:
    malicious= df['malicious'].values #store malicious column val
    df.pop('malicious')
  if 'Unnamed: 0' in df.columns.values:
    df.pop('Unnamed: 0')
    
  dfColNames= df.columns.values
  
 
  for index in df.index:
    currentApp=""
   
    for col in df:
     
      if df.loc[index,col] == 0:
        currentApp+="~"+col #get column names
    corpus.append(currentApp) 
  
  return appNames, malicious, dfColNames
# sklearn tfidf
from sklearn.feature_extraction.text import TfidfVectorizer

def reduceAfterTFIDF(reducer,df):
  print("Reducing...")
  thresholdIDF= 0.0001  #used to filter to get tfidf count for those over this threshold (tfidf= the higher the number the more important)
  thresholdSum= 0 #used to filter out those that are under this number 
  originalColVal= reducer.columns.values #store original columns from tfidf
  
  if 'malicious' in originalColVal:
    reducer.pop('malicious')
  if 'Unnamed: 0' in originalColVal:
    reducer.pop('Unnamed: 0')
  

  tf= []
 
  for col in reducer:
    important= sum(reducer[col]> thresholdIDF ) #get count for more unique/important values
    zeros= sum(reducer[col]== 0.000000) #number of columns with 0
    lessImportant= abs(sum(reducer[col] < thresholdIDF)-zeros)  #get count for more frequent/unimportant values
    thresholdSum= lessImportant-important 
    if(thresholdSum>0):
      tf.append(col) #store unimportnat values
  
  
  # if value in tf is not found in original database, pop column in final dataframe, return reduced dataframe
  
  finalDataFrame= df
  finalDataFrame= finalDataFrame.drop(columns=tf)
  tf.clear()
  return finalDataFrame

def tfIDFAlgorithm(col):
  
  def my_tokenizer(col):
    return col.split("~")

  vectorizer = TfidfVectorizer(tokenizer= my_tokenizer, lowercase= False)
  
  vectorizer.fit(col)

  result = vectorizer.fit_transform(corpus)

  # print("amm= ", len(vectorizer.get_feature_names_out()))
  return result.toarray(), vectorizer.get_feature_names_out()


def dropFrequenTerms(df):
  print("minimizing feature vector")
  completeFeatures = df
  # Using Zipf's Law
  finalDataFrame= completeFeatures
  originalColVal= df.columns.values #store original columns from tfidf

  if 'malicious' in originalColVal:
    df.pop('malicious')
  if 'Unnamed: 0' in originalColVal:
    df.pop('Unnamed: 0')
  
  originalColVal= df.columns.values #store refreshed original columns
  
  tf= pd.DataFrame(data=originalColVal, columns=["AppContains"]) #get features
  tf['appValues']= df.sum().values #get total frequency of features
  tf= tf.sort_values(by=['appValues'], ascending=False) #sort features based on freq
  tf["rank"]= np.arange(1, len(originalColVal)+1) #rank features
  
  
  #P= c /rank  c= freq/ N(total terms)  
  tf["tf"]= np.divide(tf["appValues"],  len(originalColVal))
  tf["P"]= np.divide(tf["tf"],  tf["rank"])
  #get probability and the high ranked values, drop those that MEET threshold   P< median= meet threshold
  median= tf['P'].median()
  print(median)
  tf= tf[tf["P"]>median]
  # if value in tf is not found in original database, pop column in final dataframe, return reduced dataframe

  finalDataFrame= finalDataFrame.drop(columns=tf["AppContains"].values)
  return finalDataFrame

def outputTfidf():
  
  dataframes[0].to_csv(filepaths.tfidfdataframe, na_rep=0, header=dataframes[0].columns) #output csvFile
   
  dataframes.clear()


def main():
  print('tfidf running')

  print(location)
  f = open(location, "r")
     
  read = pd.read_csv(f,  index_col=['name']) #get dataframe 
  appNames, malicious, dfColNames= createCorpus(read) #create corpus for apps
  
  tfidfR, colName= tfIDFAlgorithm(dfColNames) #run algo with corpus
  
  tfIDFFrame= pd.DataFrame(tfidfR) #get TFIDF dataframe
  tfIDFFrame.columns=colName
  tfIDFFrame = tfIDFFrame.set_index(appNames)

  dfAfter= reduceAfterTFIDF(tfIDFFrame,read)
  
  

  #which way do we want to trim the data? both so far trim by half but results are a bit differnt
  finalDataFrame=dropFrequenTerms(dfAfter) #using binary 1, 0 feature vector
  # dropFrequenTerms(tfIDFFrame) #using tfidf values
  finalDataFrame.insert(0, "malicious", malicious)
  finalDataFrame.to_csv(filepaths.cleanedDataframe, na_rep=0, header= finalDataFrame.columns) #output csvFile

def forCombinations():
  print('tfidf running for combinations')
  corpus.clear()
  print(combo)
  f = open(combo, "r")
     
  read = pd.read_csv(f,  index_col=['name']) #get dataframe 
  appNames, malicious, dfColNames= createCorpus(read) #create corpus for apps
  tfidfR, colName= tfIDFAlgorithm(dfColNames) #run algo with corpus
  
  tfIDFFrame= pd.DataFrame(tfidfR) #get TFIDF dataframe
  tfIDFFrame.columns=colName
  tfIDFFrame = tfIDFFrame.set_index(appNames)
  dfAfter= reduceAfterTFIDF(tfIDFFrame,read)
  
  

  #which way do we want to trim the data? both so far trim by half but results are a bit differnt
  finalDataFrame=dropFrequenTerms(dfAfter) #using binary 1, 0 feature vector
  # dropFrequenTerms(tfIDFFrame) #using tfidf values
  finalDataFrame.insert(0, "malicious", malicious)
  finalDataFrame.to_csv(filepaths.cleanedCombinations, na_rep=0, header= finalDataFrame.columns) #output csvFile
      
  
