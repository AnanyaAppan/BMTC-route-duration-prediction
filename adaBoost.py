from sklearn.ensemble import AdaBoostRegressor
import pandas as pd

df = pd.read_csv('encoded_grid_21_17.csv', header=None)

X, y = df(n_features=4, n_informative=2,random_state=0, shuffle=False)

regr = AdaBoostRegressor(random_state=0, n_estimators=100)

regr.fit(X, y)  

AdaBoostRegressor(base_estimator=None, learning_rate=1.0, loss='linear',n_estimators=100, random_state=0)