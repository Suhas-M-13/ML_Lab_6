from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import numpy as np
import pandas as pd

data = pd.read_csv("weather_forecast.csv")
data.head()

desired_rows= 1500
data = pd.concat([data]*(desired_rows//len(data)),ignore_index=True)
data.shape

for col in data.columns:
    data[col] = data[col].map({x : (i+1) for i,x in enumerate(data[col].unique()) })
data.head()

X = data.drop('Play', axis=1).values
Y = data['Play'].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=32)

classifier = DecisionTreeClassifier(max_depth=3)
classifier.fit(X_train, Y_train)
print(tree.export_text(classifier,max_depth=3,feature_names=list(data.columns[:-1]),class_names=['No','Yes']))
print("Accuracy: ",classifier.score(X_test,Y_test))