import dask.dataframe as dd
df = dd.read_csv("../../BMTC/train.csv", blocksize=5e6)
# df= df.set_index("150218715")
print(df.head())
print(df.count())
df.to_parquet('../../BMTC/train.parquet', engine='pyarrow')