import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("pima-data.csv")

data.info()
data.head()
data.describe()

data.columns
data.dtypes

print(data.isnull().sum())

import seaborn as sns
#get correlations of each features in dataset
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))

#plot heat map
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")

data.corr()

sns.set_style('whitegrid')
sns.countplot(x='diabetes', data=data, palette='RdBu_r')

diabetes_map = {True:1,False:0}
data['diabetes'] = data['diabetes'].map(diabetes_map)

data.head(5)

feature_columns = ['num_preg', 'glucose_conc', 'diastolic_bp', 'insulin', 'bmi', 'diab_pred', 'age','skin']
predicted_class = ['diabetes']

X = data[feature_columns].values
Y = data[predicted_class].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.20, random_state=1)

print("Number of rows missing glucose_conc:{0}".format(len(data.loc[data['glucose_conc']==0])))
print("Number of rows missing diastolic_bp:{0}".format(len(data.loc[data['diastolic_bp']==0])))
print("Number of rows missing insulin:{0}".format(len(data.loc[data['insulin']==0])))
print("Number of rows missing bmi:{0}".format(len(data.loc[data['bmi']==0])))
print("Number of rows missing diab_pred:{0}".format(len(data.loc[data['diab_pred']==0])))
print("Number of rows missing age:{0}".format(len(data.loc[data['age']==0])))
print("Number of rows missing skin:{0}".format(len(data.loc[data['skin']==0])))

from sklearn.preprocessing import Imputer
fill_values = Imputer(missing_values = 0, strategy = 'mean', axis = 0 )

X_train = fill_values.fit_transform(X_train)
X_test = fill_values.fit_transform(X_test)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=1)

model.fit(X_train,Y_train)

model.fit(X_test,Y_test)
model.score(X_test,Y_test)

model.predict(X_train)

x_demo=[[5,126,70,160,35,0.242,66,0.000]]
if model.predict(x_demo)==0:
    print("Person is likely to NOT have diabetes")
else:
    print("Person is likely to have diabetes")