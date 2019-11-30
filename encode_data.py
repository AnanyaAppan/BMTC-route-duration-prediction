import pandas as pd 

def encode_weekday(timestamp):
    last_two_year = int(timestamp[2:4])
    first_two_year = int(timestamp[0:2])
    month = int(timestamp[5:7])
    date = int(timestamp[8:10])
    encode_week = (date + ((13*month-1)/5) + last_two_year + (last_two_year/4) + (first_two_year/4) -2*first_two_year)%7
    return encode_week

def encode_time(timestamp):
    minutes = int(timestamp[11:13])*60 + int(timestamp[14:16])
    return minutes/30


chunksize = 10 ^ 6

for chunk in pd.read_csv("/home/ananya/Documents/MLLab/BMTC-route-duration-prediction/encoded_grid_21_17.csv",skiprows=1, names = ["index","busId" , "latitude", "longitude", "angle", "speed", "timestamp","gridNum"], chunksize = chunksize):

    df = pd.DataFrame(chunk)

    del df["index"]

    df["time"] = [encode_time(var) for var in df["timestamp"]]
    df["day"] = [encode_weekday(var) for var in df["timestamp"]]

    df.to_csv('final_encoded_grid_21_17.csv', mode='a', header=False)