import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('lalliTrial/encoded_grid_21_17.csv', header=None, nrows = 100000)

train=df.sample(frac=0.8,random_state=42) #random state is a seed value
test=df.drop(train.index)

X = train.iloc[:,[2,3,7,8]].values
y = train.iloc[:,5].values
X_test = test.iloc[:,[2,3,7,8]].values
y_test = test.iloc[:,5].values

poly = PolynomialFeatures(degree = 8) 
X_poly = poly.fit_transform(X)
X_poly_test = poly.fit_transform(X_test)
X_poly = StandardScaler().fit_transform(X_poly)
X_test = StandardScaler().fit_transform(X_poly_test)
print(X_poly.shape)
print(X_test.shape)

comp=20
cols = ['principal component ' + str(x) for x in range(1,comp+1)]
pca = PCA(n_components=comp)
principalComponents = pca.fit_transform(X_poly)
principalComponentsTest = pca.transform(X_test)
X_poly = pd.DataFrame(data = principalComponents , columns = cols)
X_test = pd.DataFrame(data = principalComponentsTest , columns = cols)
  
poly.fit(X_poly, y) 
lin2 = LinearRegression() 
lin2.fit(X_poly, y) 
y_poly_pred = lin2.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test,y_poly_pred))
r2 = r2_score(y_test,y_poly_pred)
print(rmse)
print(r2)

train.insert(8,"predicted_speed",y_poly_pred)

train.to_csv("fitted_21_17.csv")

# plt.scatter(X, y, s=10)
# # sort the values of x before line plot
# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(X,y_poly_pred), key=sort_axis)
# x, y_poly_pred = zip(*sorted_zip)
# plt.plot(x, y_poly_pred, color='m')
# plt.show()

