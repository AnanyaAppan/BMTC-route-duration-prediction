import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

chunksize = 5 * 10 ^ 6

for chunk in pd.read_csv('/home/ananya/Documents/BMTC/hundred/encoded_sec.csv', header=None, chunksize=chunksize):

    # train = df.sample(frac=0.8,random_state=42) #random state is a seed value
    # test = df.drop(train.index)
    train = pd.DataFrame(chunk)

    X_train = train.iloc[:,[1,2,3,7,8]].values
    y_train = train.iloc[:,4].values

    # X_test = test.iloc[:,[1,2,3,7,8]].values
    # y_test = test.iloc[:,4].values

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)

    regressor = RandomForestRegressor(n_estimators=90, random_state=42)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_train)

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_pred)))

    train.insert(9,"predicted_speed",y_pred)

    train.to_csv("/home/ananya/Documents/BMTC/hundred/fitted_hundred.csv",header=False, index=False,mode='a')

