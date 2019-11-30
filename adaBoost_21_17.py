import numpy as np 
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

df = pd.read_csv('lalliTrial/grid_21_17.csv', names=["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"], nrows = 100000)

X = df.drop(columns=["busId", "speed", "timestamp"])
y = df["speed"].values


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

regressor = AdaBoostRegressor(n_estimators=10, random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print ('score:', regressor.score(X_test, y_test))
