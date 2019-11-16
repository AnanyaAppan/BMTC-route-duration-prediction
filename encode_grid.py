from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import sys
import pandas as pd
from pyspark.sql.functions import monotonically_increasing_id

filename = "filtered_sorted_partaa.csv"

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

final_df = df.withColumn("encoded_grid",listGrid)
final_df.to_csv("../BMTC_sorted/filtered_encoded_partaa.csv")


