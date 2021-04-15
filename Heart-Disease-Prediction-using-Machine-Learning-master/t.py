import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import accuracy_score
print(os.listdir())

import warnings
warnings.filterwarnings('ignore')


dataset = pd.read_csv("heart.csv")


dataset["target"].describe()
dataset["target"].unique()
y = dataset["target"]

sns.countplot(y)


target_temp = dataset.target.value_counts()

print(target_temp)

print("Percentage of patience without heart problems: "+str(round(target_temp[0]*100/303,2)))
print("Percentage of patience with heart problems: "+str(round(target_temp[1]*100/303,2)))

dataset["sex"].unique()

from sklearn.model_selection import train_test_split

predictors = dataset.drop("target",axis=1)
target = dataset["target"]
inp=[[70,1,0,130,322,0,0,109,0,2.4,1,3,2],]
hea=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
df = pd.DataFrame(inp, columns =hea)
print('dataframe',df)
X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=0)
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

nb.fit(X_train,Y_train)

Y_pred_nb = nb.predict(df)

if Y_pred_nb == 1:
    print("The patient has heart disease!")
elif Y_pred_nb ==0:
    print("The patient doesn't have heart disease!\n")
