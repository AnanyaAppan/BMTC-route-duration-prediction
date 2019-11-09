import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import sys

# filename = "../../BMTC/sorted_data/" + sys.argv[1]
filename = "../../BMTC/filtered_zero_removed.csv"
df = pd.read_csv(filename, names = ["busId" , "latitude", "longitude", "angle", "speed", "timestamp"])

lat = list(map(float,df.latitude.tolist()[1:]))
long = list(map(float,df.longitude.tolist()[1:]))

print(lat)

plt.scatter(lat,long,marker='.')

plt.show()