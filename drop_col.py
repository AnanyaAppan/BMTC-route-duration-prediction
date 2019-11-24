import pandas as pd 


chunksize = 10 ** 6

for chunk in pd.read_csv("/home/ananya/Documents/BMTC/sorted_encoded_data/final_encoded.csv", names = ["index","busId","latitude","longitude","angle","speed", "timestamp", "gridnum", "time", "day" ], chunksize = chunksize):
    df = pd.DataFrame(chunk)
    # print(df.head())
    del df["time"]
    df["time"] = [int(var[11:13])*60*60 + int(var[14:16])*60 + int(var[17:19]) for var in df["timestamp"]]
    df.to_csv("/home/ananya/Documents/BMTC/final/encoded_sec.csv", mode='a', header=False, index = False)