import pandas as pd

chunksize = 10 ** 3
ndx = 1 

for chunk in pd.read_csv("../sorted_partya.csv", names = ["busId" , "latitude", "longitude",  "angle", "speed", "timestamp"], chunksize=chunksize):
    df = pd.DataFrame(chunk)
    change_index = 0
    remove_indices = []
    while ndx < chunksize - 2:
        df_0 = pd.DataFrame(chunk.iloc[ndx-1]).transpose()
        df_1 = pd.DataFrame(chunk.iloc[ndx]).transpose()
        df_2 = pd.DataFrame(chunk.iloc[ndx+1]).transpose()
        if df_1.speed[ndx] == 0:
            if df_0.speed[ndx-1] == 0 and df_2.speed[ndx+1] == 0 and df_0.angle[ndx-1] == df_1.angle[ndx] and df_1.angle[ndx] == df_2.angle[ndx+1]:
                remove_indices.append(ndx)
        ndx += 1
    for var in remove_indices:
        df = df.drop(df.index[var - change_index])
        change_index += 1
    df.to_csv('../zero_removed.csv', mode='a', header=False)#\\, index = False)

    
    