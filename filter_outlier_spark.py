from pyspark.sql import SparkSession
import sys

filename = "../sorted_partya.csv"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="false").toDF("busId" , "latitude", "longitude", "angle", "speed", "timestamp")
# Displays the content of the DataFrame to stdout
df.printSchema()
print("starting to filer...\n")
df_filtered = df.filter((df.latitude > 10) & (df.latitude < 15) & (df.longitude > 75) & (df.longitude < 80))
df_filtered.show()
df_filtered.toPandas().to_csv('../filtered_.csv')
