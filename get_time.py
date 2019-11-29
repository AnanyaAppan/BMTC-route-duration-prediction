import math
from pyspark.sql import SparkSession
import sys
from encode_data import encode_weekday
from encode_data import encode_time
from get_grid import get_grid
from get_grid import sub_grid
from datetime import datetime
from datetime import timedelta
import pandas as pd
 

filename = "/home/ananya/Documents/BMTC/final/fitted_final_grouped.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

chunksize = 10**5


def get_time(lat1, lon1, lat2, lon2, timestamp):
    radius = 6371
    dLat = (math.pi/180)*(lat2-lat1)
    dLon = (math.pi/180)*(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos((math.pi/180)*(lat1)) * math.cos((math.pi/180)*(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # distance in km
    distance = radius * c
    avg_speed = 0
    for chunk in pd.read_csv(filename,header=None,names = ["grid","subgrid","day","time","speed"], chunksize=chunksize):
        
        pdf = pd.DataFrame(chunk)
        # print(pdf.head())
        df = spark.createDataFrame(pdf)
        # df.show()
        df1 = df.filter((df.grid <= get_grid(lat1, lon1)) & (df.subgrid <= sub_grid(lat1, lon1)) & (df.day <= encode_weekday(timestamp)) & (df.time <= encode_time(timestamp))).toPandas()
        df2 = df.filter((df.grid <= get_grid(lat2, lon2)) & (df.subgrid <= sub_grid(lat2, lon2)) & (df.day <= encode_weekday(timestamp)) & (df.time <= encode_time(timestamp))).toPandas()
        
        df1 = df1.sort_values('grid')
        df1 = df1.sort_values('subgrid')
        df1 = df1.sort_values('day')
        df1 = df1.sort_values('time')

        df2 = df2.sort_values('grid')
        df2 = df2.sort_values('subgrid')
        df2 = df2.sort_values('day')
        df2 = df2.sort_values('time')

        speed1 = 0
        speed2 = 0

        if(len(df1)): speed1 = df1.iloc[len(df1)-1].speed
        if(len(df2)): speed2 = df2.iloc[len(df2)-1].speed
        if(len(df1) or len(df2)): avg_speed = (speed1+speed2) / 2

    # time in hours
    time = (distance/avg_speed)*3600 
    print(time)
    return time

def increment_timestamp(time, timestamp):
    print("time = ",time)
    print("timestamp = ",timestamp)
    datetimeObj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return str(datetimeObj + timedelta(seconds = time))

def get_total_time(lat_long, timestamp):
    time = 0
    for i in range(len(lat_long)-1):
        lat1, lon1 = map(float, lat_long[i].split(":"))
        lat2, lon2 = map(float, lat_long[i+1].split(":"))
        temp_time = get_time(lat1, lon1, lat2, lon2, timestamp)
        time += temp_time
        timestamp = increment_timestamp(temp_time, timestamp)
    return time,timestamp

increment_timestamp(345.78,'2016-07-01 00:06:10')
for chunk in pd.read_csv('/home/ananya/Documents/BMTC/test.csv', header=None, chunksize=chunksize,skiprows=1):
    df = pd.DataFrame(chunk)
    final_time = []
    final_timestamp = []
    for i in range(len(df)):
        row = df.iloc[i].values
        timestamp = row[1].strip()
        lat_long = row[2:]
        # print("timestamp = ",timestamp)
        # print("lat_long = ",lat_long)
        f_time,f_timestamp = get_total_time(lat_long, timestamp)
        final_time.append(f_time)
        final_timestamp.append(f_timestamp)
    df.insert(103,"final_time",final_time)
    df.insert(104,"final_timestamp",final_timestamp)
    df.to_csv("/home/ananya/Documents/BMTC/final/test_final.csv",header=False, index=False,mode='a')





    