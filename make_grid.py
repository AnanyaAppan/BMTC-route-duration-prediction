from pyspark.sql import SparkSession
import sys

filename = "../../BMTC/filtered_data/" + sys.argv[1]

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,format="csv", sep=",", inferSchema="true", header="false").toDF("busId" , "latitude", "longitude", "angle", "speed", "timestamp")
# Displays the content of the DataFrame to stdout
df.printSchema()
length_lat = 0.0032
length_long = 0.0043
lat = 13.0218
long = 77.551796

while(lat < 13.32):
    while(long < 78):
        print("nkdjnjs  ", lat+length_lat)
        df_filtered = df.filter((df.latitude > lat) & (df.latitude < lat+length_lat) & (df.longitude > long) & (df.longitude < long+length_long))
        long += length_long
        df_filtered.toPandas().to_csv('../../BMTC/gridData/grid_'+filename, mode='a', header=False)
        exit(0)
    lat += length_lat

# df_filtered.show()
# df_filtered.toPandas().to_csv("../../BMTC/filtered_zero_removed.csv")


