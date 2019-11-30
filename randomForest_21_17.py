import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

chunksize = 10**5  

# for chunk in pd.read_csv('lalliTrial/grid_21_17.csv', names=["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"], nrows = 100000, chunksize=chunksize): #,skiprows=164399999):

#     df = pd.DataFrame(chunk)
#     X = df.drop(columns=["busId", "speed", "timestamp"])
#     y = df["speed"].values

#     X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42)

#     sc = StandardScaler()
#     X_train = sc.fit_transform(X_train)
#     X_test = sc.transform(X_test)

#     regressor = RandomForestRegressor(n_estimators=90, random_state=42)
#     regressor.fit(X_train, y_train)
#     y_pred = regressor.predict(X_train)

#     print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
#     print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
#     print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    # train.insert(10,"predicted_speed",y_pred)

    # train.to_csv("/home/ananya/Documents/BMTC/final/fitted_final.csv",header=False, index=False,mode='a')

df = pd.read_csv('lalliTrial/grid_21_17.csv', names=["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"], nrows = 100000)
X = df.drop(columns=["busId", "speed", "timestamp"])
y = df["speed"].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

regressor = RandomForestRegressor(n_estimators=90, random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))