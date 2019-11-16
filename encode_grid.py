from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import sys
import pandas as pd
from pyspark.sql.functions import monotonically_increasing_id

filename = "/media/slr/TOSHIBA EXT/filtered_data/filtered_sorted_partaa.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="false").toDF("Index","busId" , "latitude", "longitude", "angle", "speed", "timestamp")
# Displays the content of the DataFrame to stdout
df.printSchema()
length_lat = 0.032/2
length_long = 0.043/2
# i rows 42
i = 0
# j columns 34
j = 0

lat = 12.66 
long = 77.27 

listGrid = []
while(lat < 13.32):
    while(long < 78):
        listGrid.append((i*34) + 42)
        long += length_long
        j += 1
    i += 1
    j = 0
    lat += length_lat

df_grid = SQLContext.createDataFrame([(l,) for l in listGrid], ['grid_value'])
df = df.withColumn("row_idx", monotonically_increasing_id())
df_grid = df_grid.withColumn("row_idx", monotonically_increasing_id())
final_df = df.join(df_grid, df.row_idx == df_grid.row_idx).\
             drop("row_idx")
final_df.to_csv("../BMTC_sorted/filtered_encoded_partaa.csv")


