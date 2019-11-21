import math
from pyspark.sql import SparkSession
import sys
from encode_data import encode_weekday
from encode_data import encode_time
from get_grid import get_grid
from get_grid import sub_grid
from datetime import datetime
from datetime import timedelta


filename = "../sorted_partya.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

def get_time(lat1, lon1, lat2, lon2, timestamp):
    radius = 6371
    dLat = (math.pi/180)*(lat2-lat1)
    dLon = (math.pi/180)*(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos((math.pi/180)*(lat1)) * math.cos((math.pi/180)*(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # distance in km
    distance = radius * c
    df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="false").toDF("grid","subgrid","day","time","speed")
    speed1 = df.filter((df.grid == get_grid(lat1, lon1)) & (df.subgrid == sub_grid(lat1, lon1)) & (df.day == encode_weekday(timestamp)) & (df.time == encode_time(timestamp))).select("speed")
    speed2 = df.filter((df.grid == get_grid(lat2, lon2)) & (df.subgrid == sub_grid(lat2, lon2)) & (df.day == encode_weekday(timestamp)) & (df.time == encode_time(timestamp))).select("speed")
    avg_speed = (speed1 + speed2)/2
    # time in hours
    time = (distance/avg_speed)*3600 
    return time

def increment_timestamp(time, timestamp):
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
    return time

increment_timestamp(60*60*24,'2016-07-01 00:06:10')






    