import pandas as pd

chunksize = 10 ** 5
count = 0
for chunk in pd.read_csv("train.csv", chunksize=chunksize):
    print(chunk.head())
    i = 0
    while i < chunksize:
        bus = chunk.take([0], axis=1).iloc[i].values[0]
        df = pd.DataFrame(chunk.iloc[i]).transpose()
        df.to_csv('file ' + str(bus) + '.csv', mode='a', header=False)
        i += 1
    count += 1
