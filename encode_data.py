import pandas as pd 


chunk = pd.read_csv("grid_21_17_zero_removed.csv", names = ["index","busId" , "latitude", "longitude", "angle", "speed", "timestamp","gridNum"])
df = pd.DataFrame(chunk)

df["time"] = [int(var[11:13])*60 + int(var[14:16]) for var in df["timestamp"]]

print(df["time"])

df.to_csv('encoded_grid_21_17.csv', mode='a', header=False, index = False)