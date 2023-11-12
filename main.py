# Importing dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
# Including & Reading the CSV file:
df = pd.read_csv("tumor_data.csv")
#dropping unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
x = df.drop('diagnosis', axis=1)
y = df['diagnosis']

def randomForest(X_train,y_train,X_test,y_test):
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    y_pred = rfc.predict(X_test)
    return(accuracy_score(y_test, y_pred))
 

def decisionTree(X_train,y_train,X_test,y_test):
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    y_pred = dtc.predict(X_test)
    return (accuracy_score(y_test, y_pred))
 
def logRegression(X_train,y_train,X_test,y_test):
    # apply Logistic Regression
    
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    
    # implemented our model through logistic regression
    y_pred = lr.predict(X_test)
    return accuracy_score(y_test,y_pred)

def SVMClassifier(X_train,y_train,X_test,y_test):
    svc = svm.SVC()
    svc.fit(X_train,y_train)
    y_pred = svc.predict(X_test)
    return (accuracy_score(y_test, y_pred))


# divide the dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
  
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
logRegressionAccuracy=logRegression(X_train,y_train,X_test,y_test)
decisionTreeAccuracy=decisionTree(X_train,y_train,X_test,y_test)
randomForestAccuracy=randomForest(X_train,y_train,X_test,y_test)
SVMClassifierAccuracy=SVMClassifier(X_train,y_train,X_test,y_test)

#tabulating the results
tempResults = pd.DataFrame({'Algorithm':['Logistic Regression Method'], 'Accuracy':[logRegressionAccuracy]})
results=pd.DataFrame()
results = pd.concat([results, tempResults])
results = results[['Algorithm','Accuracy']]
tempResults = pd.DataFrame({'Algorithm': ['Decision tree Classifier Method'],'Accuracy': [decisionTreeAccuracy]})
results = pd.concat([results, tempResults])

tempResults = pd.DataFrame({'Algorithm': ['Random Forest Classifier Method'], 'Accuracy': [randomForestAccuracy]})
results = pd.concat([results, tempResults])
tempResults = pd.DataFrame({'Algorithm': ['Support Vector Classifier Method'],'Accuracy': [SVMClassifierAccuracy]})
results = pd.concat([results, tempResults])
print(results)

