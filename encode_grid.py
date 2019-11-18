from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import sys
import pandas as pd
from pyspark.sql.functions import monotonically_increasing_id

filename = "../../BMTC/filtered_data/" + sys.argv[1]

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="true").toDF("Index","busId" , "latitude", "longitude", "angle", "speed", "timestamp")
# Displays the content of the DataFrame to stdout
length_lat = 0.032/2
length_long = 0.043/2
# i rows 42
i = 0
# j columns 34
j = 0

lat = 12.66 
long = 77.27 

df_encoded = df.select('*', (((df.latitude-lat)/length_lat).cast("int") * 34 + ((df.longitude-long)/length_long).cast("int")).alias('grid_num'))
# df_encoded.show()

df_encoded.toPandas().to_csv("../../BMTC/encoded_data/encoded_"+ sys.argv[1],header=False, index = False)
