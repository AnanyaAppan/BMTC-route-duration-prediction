import dask.dataframe as dd
df = dd.read_csv("weatherdata.csv", blocksize=50e6)
df= df.set_index("temperature")
print(df.head())