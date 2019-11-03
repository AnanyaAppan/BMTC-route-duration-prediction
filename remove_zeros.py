import pandas as pd

remove_indices = []
chunksize = 10 ** 5
ndx = 1

chunk = pd.read_csv("../BMTC_sorted/sorted_partya.csv", names = ["busId" , "latitude", "longitude", "angle", "speed", "timestamp"])
df = pd.DataFrame(chunk)
while ndx < chunksize - 2:
    df_0 = pd.DataFrame(df.iloc[ndx-1]).transpose()
    df_1 = pd.DataFrame(df.iloc[ndx]).transpose()
    df_2 = pd.DataFrame(df.iloc[ndx+1]).transpose()
    if df_1.speed[ndx] == 0:
        if df_0.speed[ndx-1] == 0 and df_2.speed[ndx+1] == 0 and df_0.angle[ndx-1] == df_1.angle[ndx] and df_1.angle[ndx] == df_2.angle[ndx+1]:
            remove_indices.append(ndx)

    ndx += 1

for ndx in remove_indices:
    df.at[ndx,'speed'] = -100

print(df.iloc[10:40])

ndx = 0
changed_indices = 0
while ndx < chunksize:
    if df.at[ndx,'speed'] == -100:
        df = df.drop(df.index[ndx - changed_indices])
        changed_indices += 1
    ndx += 1


df.to_csv('../zero_removed.csv', mode='a', header=False)#\\, index = False)

print(remove_indices)

    
    