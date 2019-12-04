import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import sys

# filename = "../../BMTC/sorted_data/" + sys.argv[1]
filename = "/home/ananya/Documents/BMTC/final_bmtc_test_data.csv"
df = pd.read_csv(filename)

for i in range(4):
    row = df.iloc[i].values 
    lat_long = row[2:]
    lat = []
    long = []
    for i in lat_long:
        x,y = i.strip().split(":")
        lat.append(float(x))
        long.append(float(y))

    # plt.scatter(angle,speed,marker='.')
    plt.plot(lat,long,marker='.')

    plt.show()
