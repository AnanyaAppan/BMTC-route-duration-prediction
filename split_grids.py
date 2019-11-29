from pyspark.sql import SparkSession
import pandas as pd

filename = "/home/ananya/Documents/BMTC/final/fitted_final_grouped.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

chunksize = 10**5