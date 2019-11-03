import pandas as pd

chunksize = 32806
for chunk in pd.read_csv("../BMTC_sorted/final_sorted.csv", chunksize=chunksize):
    df = pd.DataFrame(chunk)
    df.to_csv('~/Desktop/ML/Project/BMTC_sorted/train.csv', mode='a', header=False)
    break
