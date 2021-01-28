import joblib
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# print("starting.. ")

data = sns.load_dataset("iris")
# print("dataset imported..")

print(data)

# print("separate dependent and independent variables..")
X = data.drop(['species'], axis=1)
y = data['species']

# print("intialize & fit model..")
knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X, y)

joblib.dump(knn, "./knn.joblib")

print('predict.. ')
print(knn.predict([[6, 3, 4, 2]]))