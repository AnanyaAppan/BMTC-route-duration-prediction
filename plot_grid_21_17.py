import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import sys

# filename = "../../BMTC/sorted_data/" + sys.argv[1]
filename = "grid_21_17_zero_removed.csv"
df = pd.read_csv(filename, names = ["Index", "busId" , "latitude", "longitude", "angle", "speed", "timestamp"])

lat = list(map(float,df.latitude.tolist()[1:]))
long = list(map(float,df.longitude.tolist()[1:]))
angle = list(map(float,df.angle.tolist()[1:]))
speed = list(map(float,df.speed.tolist()[1:]))


plt.scatter(speed,angle,marker='.')
# plt.plot(speed,angle,linewidth=2.0)

plt.show()