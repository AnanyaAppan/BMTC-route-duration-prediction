import pandas as pd 


chunksize = 10 ** 6

for chunk in pd.read_csv("/home/ananya/Documents/BMTC/hundred/train_encoded_hundred.csv", names = ["busId","latitude","longitude","angle","speed", "timestamp", "gridnum", "time", "day" ], chunksize = chunksize):
    df = pd.DataFrame(chunk)
    del df["time"]
    df["time"] = [int(var[11:13])*60*60 + int(var[14:16])*60 + int(var[17:19]) for var in df["timestamp"]]
    df.to_csv("/home/ananya/Documents/BMTC/hundred/encoded_sec.csv", mode='a', header=False, index = False)