# from pyspark.sql import SparkSession
import pandas as pd

filename = "/home/ananya/Documents/BMTC/final/fitted_final_grouped.csv"

# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()

chunksize = 10**5

for chunk in pd.read_csv(filename,header=None,names = ["grid","subgrid","day","time","speed"], chunksize=chunksize):

    df = pd.DataFrame(chunk)
    for i, g in df.groupby("grid"):
        g.to_csv('/home/ananya/Documents/BMTC/final/{}.csv'.format(i), header=False, index_label=False)