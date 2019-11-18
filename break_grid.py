import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

filename = "../../BMTC/sorted_encoded_data/final_sorted.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="false").toDF("Index","busId" , "latitude", "longitude", "angle", "speed", "timestamp","grid_num")

df.write.partitionBy("grid_num").saveAsTable("myparquet")
