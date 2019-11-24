import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics


chunksize = 10**5
total = 0

for chunk in pd.read_csv('/home/ananya/Documents/BMTC/final/fitted_final.csv', header=None, chunksize=chunksize,skiprows=1):
    df = pd.DataFrame(chunk)
    print(df.iloc[0])
    break

# print(total)
    