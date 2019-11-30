import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('lalliTrial/grid_21_17.csv', names=["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"], nrows = 100000)

X = df.drop(columns=["busId", "speed", "timestamp"])
y = df["speed"].values


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=42)


poly = PolynomialFeatures(degree = 8) 
X_poly = poly.fit_transform(X_train)
X_poly_test = poly.fit_transform(X_test)
X_poly = StandardScaler().fit_transform(X_poly)
X_test = StandardScaler().fit_transform(X_poly_test)
# print(X_poly.shape)
# print(X_test.shape)

comp=20
cols = ['principal component ' + str(x) for x in range(1,comp+1)]
pca = PCA(n_components=comp)
principalComponents = pca.fit_transform(X_poly)
principalComponentsTest = pca.transform(X_test)
X_poly = pd.DataFrame(data = principalComponents , columns = cols)
X_test = pd.DataFrame(data = principalComponentsTest , columns = cols)
  
poly.fit(X_poly, y_train) 
lin2 = LinearRegression() 
lin2.fit(X_poly, y_train) 
y_poly_pred = lin2.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test,y_poly_pred))
r2 = r2_score(y_test,y_poly_pred)
print(rmse)
print(r2)

# train.insert(8,"predicted_speed",y_poly_pred)

# train.to_csv("fitted_21_17.csv")

# plt.scatter(X, y, s=10)
# # sort the values of x before line plot
# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(X,y_poly_pred), key=sort_axis)
# x, y_poly_pred = zip(*sorted_zip)
# plt.plot(x, y_poly_pred, color='m')
# plt.show()
