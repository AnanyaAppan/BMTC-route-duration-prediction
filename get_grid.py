from pyspark.sql import SparkSession
import sys

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

def get_half_hour(time):
    return (time/30).cast("int")

filename = "lalliTrial/final_encoded.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# # spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header=True).toDF("busId" , "latitude", "longitude", "angle", "speed", "timestamp","grid_num","time","day")
# # df.show()
df.groupBy("grid_num",(subgrid(df.latitude,df.longitude)).alias("subgrid"),get_half_hour(df.time).alias("half_hour"), "day").avg("speed").show()