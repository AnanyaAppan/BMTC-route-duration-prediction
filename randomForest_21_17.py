import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

df = pd.read_csv('lalliTrial/encoded_grid_21_17.csv', header=None, nrows = 10000)

train = df.sample(frac=0.8,random_state=42) #random state is a seed value
test = df.drop(train.index)

X_train = train.iloc[:,[2,3,7,8]].values
y_train = train.iloc[:,5].values

X_test = test.iloc[:,[2,3,7,8]].values
y_test = test.iloc[:,5].values

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

regressor = RandomForestRegressor(n_estimators=90, random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

