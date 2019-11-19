import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('lalliTrial/encoded_grid_21_17.csv', header=None, names = ["index", "busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"])

del df["index"]

test_bus_ids = df.busId.unique()[-61:-1]

print(len(test_bus_ids))
# print(len(df))

# print(df.loc[204790, "busId"] in test_bus_ids)
# print (pd.DataFrame(df.loc[0]).T)

# for var in range(len(df)):
#     temp_df = pd.DataFrame(df.loc[var]).T
#     if(df.loc[var, "busId"] in test_bus_ids):
#         temp_df.to_csv('lalliTrial/test_encoded_grid_21_17.csv', mode='a', header=False, index = False)
#     else:   
#         temp_df.to_csv('lalliTrial/train_encoded_grid_21_17.csv', mode='a', header=False, index = False)

df1 = pd.read_csv('lalliTrial/test_encoded_grid_21_17.csv', header=None, names = ["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"])
df2 = pd.read_csv('lalliTrial/train_encoded_grid_21_17.csv', header=None, names = ["busId" , "latitude", "longitude", "angle", "speed", "timestamp", "time", "day"])

print (df1.busId.unique())
# print (len(df2.busId.unique()))
