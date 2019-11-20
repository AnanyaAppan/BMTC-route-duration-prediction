import pandas as pd 

def encode_weekday(timestamp):
    last_two_year = int(timestamp[2:4])
    first_two_year = int(timestamp[0:2])
    month = int(timestamp[5:7])
    date = int(timestamp[8:10])
    encode_week = (date + ((13*month-1)/5) + last_two_year + (last_two_year/4) + (first_two_year/4) -2*first_two_year)%7
    return encode_week

chunksize = 10 ** 6
var = 0
ndx = True
for chunk in pd.read_csv("grid_21_17.csv",skiprows=0, names = ["index","busId" , "latitude", "longitude", "angle", "speed", "timestamp","gridNum"], chunksize = chunksize):

    df = pd.DataFrame(chunk)

    del df["index"]

    df["time"] = [int(var[11:13])*60 + int(var[14:16]) for var in df["timestamp"]]
    df["day"] = [encode_weekday(var) for var in df["timestamp"]]

    if var == 0:
        ndx = False
        var += 1
    df.to_csv('lalliTrial/encoded_grid_21_17.csv', mode='a', header=False, index = ndx)