from pyspark.sql import SparkSession
import sys

filename = sys.argv[1]

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.load(filename,
                     format="csv", sep=",", inferSchema="true", header="true")
# Displays the content of the DataFrame to stdout
# df.show()
# df.printSchema()

df_filtered = df.filter(df.temperature > 30)
# df_filtered.show()
df_filtered.toPandas().to_csv('filtered_'+filename)