import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import accuracy_score
print(os.listdir())
import warnings
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
def heart(l):
    dataset = pd.read_csv("back/heart.csv")
    y = dataset["target"]
    target_temp = dataset.target.value_counts()
    predictors = dataset.drop("target",axis=1)
    target = dataset["target"]
    inp=[]
    inp.append(l)
    hea=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
    df = pd.DataFrame(inp, columns =hea)
    print('dataframe',df)
    X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=0)


    nb = GaussianNB()

    nb.fit(X_train,Y_train)

    Y_pred_nb = nb.predict(df)

    return Y_pred_nb
    
