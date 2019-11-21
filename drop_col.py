import pandas as pd 


chunksize = 10 ** 6

for chunk in pd.read_csv(filepath + "encoded_hundred.csv", names = ["index1", "busId", "latitude", "longitude", "angle", "speed", "timestamp", "gridNum", "time", "day"], chunksize = chunksize):