import pandas as pd

chunksize = 10 ** 6
ndx = 1 
remove_indices = []
num = 0

# i rows 42
i = 21
# j columns 34
j = 17
lat = 12.66
long = 77.27 
length_lat = 0.032/2
length_long = 0.043/2

for i in range(21,31):
    print(i)
    for chunk in pd.read_csv("../../BMTC/sorted_encoded_data/final_sorted.csv", names = ["Index","busId" , "latitude", "longitude", "angle", "speed", "timestamp","grid_num"], chunksize=chunksize):
        chunk.loc[(chunk["grid_num"] >= i*34+17) & (chunk["grid_num"] <= i*34+26)].to_csv('hundred.csv', mode='a', header=False, index = False)






