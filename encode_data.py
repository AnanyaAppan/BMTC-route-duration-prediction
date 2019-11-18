import pandas as pd 

def encode_weekday(timestamp):
    last_two_year = int(timestamp[2:4])
    first_two_year = int(timestamp[0:2])
    month = int(timestamp[5:7])
    date = int(timestamp[8:10])
    encode_week = (date + ((13*month-1)/5) + last_two_year + (last_two_year/4) + (first_two_year/4) -2*first_two_year)%7
    return encode_week

chunk = pd.read_csv("grid_21_17_zero_removed.csv", names = ["Index","busId" , "latitude", "longitude", "angle", "speed", "timestamp"])
df = pd.DataFrame(chunk)

df["time"] = [int(var[11:13])*60 + int(var[14:16]) for var in df["timestamp"]]
df["day"] = [encode_weekday(var) for var in df["timestamp"]]

print(df["time"])

df.to_csv('lalliTrial/encoded_grid_21_17.csv', mode='a', header=False, index = False)