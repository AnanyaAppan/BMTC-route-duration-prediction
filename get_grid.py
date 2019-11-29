from pyspark.sql import SparkSession
import sys
import pandas as pd
import pyspark.sql.functions as f

length_lat = 0.032/2
length_long = 0.043/2

lat = 12.66 
long = 77.27 
# Assuming the origin is (lat, long), coming up with grid number

def get_grid(lat_test, long_test):
    grid_i = int(((lat_test-lat)/length_lat))
    grid_j = int(((long_test-long)/length_long))
    grid_num = grid_i * 34 + grid_j
    return grid_num

def sub_grid(lat_test, long_test):
    grid_i = int(((lat_test-lat)/length_lat))
    grid_j = int(((long_test-long)/length_long))
    grid_lat = 12.66 + grid_i*(length_lat)
    grid_long = 77.27 + grid_j*(length_long)
    grid_length_lat = length_lat/10
    grid_length_long = length_long/10
    subgrid_i = int(((lat_test-grid_lat)/grid_length_lat))
    subgrid_j = int(((long_test-grid_long)/grid_length_long))
    subgrid_num = subgrid_i*10 + subgrid_j
    return subgrid_num


def subgrid(lat_test, long_test):
    grid_i = (((lat_test-lat)/length_lat)).cast("int")
    grid_j = (((long_test-long)/length_long)).cast("int")
    grid_lat = 12.66 + grid_i*(length_lat)
    grid_long = 77.27 + grid_j*(length_long)
    grid_length_lat = length_lat/10
    grid_length_long = length_long/10
    subgrid_i = (((lat_test-grid_lat)/grid_length_lat)).cast("int")
    subgrid_j = (((long_test-grid_long)/grid_length_long)).cast("int")
    subgrid_num = subgrid_i*10 + subgrid_j
    return subgrid_num

def get_min(time):
    return (time/60).cast("int")

# filename = "/home/ananya/Documents/BMTC/final/fitted_final.csv"

# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()

# chunksize = 10**5

# cols = ["index","busid","latitude", "longitude", "angle", "speed", "timestamp", "gridnum", "day", "time","predicted_speed"]

# for chunk in pd.read_csv(filename,header=None,names = cols, chunksize=chunksize):
#     pdf = pd.DataFrame(chunk)
#     df = spark.createDataFrame(pdf)
#     df = df.groupBy(df.gridnum,(subgrid(df.latitude,df.longitude)).alias("subgrid"),df.day,get_min(df.time).alias("minutes")).agg({"predicted_speed":"avg"})
#     #avg(df._11)
#     df.toPandas().to_csv("/home/ananya/Documents/BMTC/final/fitted_final_grouped.csv",header=False, index=False,mode='a')