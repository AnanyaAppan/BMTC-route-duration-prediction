from pyspark.sql import SparkSession
import sys

filename = "../../BMTC/filtered_data/" + sys.argv[1]

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
i = 21
# j columns 34
j = 17
lat = 12.66 + 21*length_lat
long = 77.27 + 17*length_long

# while(lat < 13.32):
#     while(long < 78):
#         if(i==21 and j==17):
#             df_filtered = df.filter((df.latitude > lat) & (df.latitude < lat+length_lat) & (df.longitude > long) & (df.longitude < long+length_long))
#             df_filtered.toPandas().to_csv('../../BMTC/gridData/grid_'+str(i)+'_'+str(j)+'.csv', mode='a', header=False, index=False)
#         long += length_long
#         j += 1
#     i += 1
#     j = 0
#     lat += length_lat

df_filtered = df.filter((df.latitude > lat) & (df.latitude < lat+length_lat) & (df.longitude > long) & (df.longitude < long+length_long))
df_filtered.toPandas().to_csv('../../BMTC/gridData/grid_'+str(i)+'_'+str(j)+'.csv', mode='a', header=False, index=False)



