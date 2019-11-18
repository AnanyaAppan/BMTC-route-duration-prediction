import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('lalliTrial/encoded_grid_21_17.csv', header=None, names = ["index", "busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"])

del df["index"]

test_bus_ids = df.busId.unique()[:60]

print(len(test_bus_ids))
# print(len(df))

# print(df.loc[204790, "busId"] in test_bus_ids)
for var in range(len(df)):
    if(df.loc[var, "busId"] in test_bus_ids):
        df.loc[var].to_csv('lalliTrial/test_encoded_grid_21_17.csv', mode='a', header=False, index = False)
    else:   
        df.loc[var].to_csv('lalliTrial/train_encoded_grid_21_17.csv', mode='a', header=False, index = False)