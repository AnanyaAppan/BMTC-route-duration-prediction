import operator
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('encoded_grid_21_17.csv', header=None, nrows = 100000)

train=df.sample(frac=0.8,random_state=200) #random state is a seed value
test=df.drop(train.index)

X = train.iloc[:,[2,3,4,7]].values
y = train.iloc[:,5].values
print(X.shape)
print(y.shape)

poly = PolynomialFeatures(degree = 7) 
X_poly = poly.fit_transform(X)
X_poly = StandardScaler().fit_transform(X_poly)
print(X_poly.shape)

comp=20
cols = ['principal component ' + str(x) for x in range(1,comp+1)]
pca = PCA(n_components=comp)
principalComponents = pca.fit_transform(X_poly)
X_poly = pd.DataFrame(data = principalComponents , columns = cols)
  
poly.fit(X_poly, y) 
lin2 = LinearRegression() 
lin2.fit(X_poly, y) 
y_poly_pred = lin2.predict(X_poly)

rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
r2 = r2_score(y,y_poly_pred)
print(rmse)
print(r2)

# plt.scatter(X, y, s=10)
# # sort the values of x before line plot
# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(X,y_poly_pred), key=sort_axis)
# x, y_poly_pred = zip(*sorted_zip)
# plt.plot(x, y_poly_pred, color='m')
# plt.show()

