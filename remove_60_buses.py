import pandas as pd 

busId = [150218622, 150219820, 150814442, 150221816, 150221298, 150221295, 150222058, 150219884, 150220607, 150813618, 150218085, 150812912, 150222113, 150219731, 150811567, 150811277, 150222320, 150222076, 150218225, 150220276, 150222876, 150219058, 150222690, 150222938, 150221304, 150219042, 150221435, 150811366, 150218960, 150219903, 150810490, 150221099, 150222606, 150222406, 150813920, 150218576, 150222082, 150814482, 150218092, 150814725, 150220081, 150218902, 150220220, 150219162, 150222045, 150218456, 150220069, 150221720, 150220322, 150222810, 150218181, 150219120, 150812841, 150222708, 150220199, 150222971, 150220198, 150813833, 150222474, 150220548]
filepath = "/home/ananya/Documents/BMTC/hundred/"

chunksize = 10 ** 6


for chunk in pd.read_csv(filepath + "encoded_hundred.csv", names = ["index1", "busId", "latitude", "longitude", "angle", "speed", "timestamp", "gridNum", "time", "day"], chunksize = chunksize):
    df = pd.DataFrame(chunk)

    del df["index1"]

    for col, val in df.iterrows(): 
        temp_df = pd.DataFrame(val).T
        if(int(val[0]) in busId):
            temp_df.to_csv(filepath + "buses/" + str(val[0]) + ".csv", mode='a', header=False, index = False)
        # else:
        #     temp_df.to_csv(filepath + "train_hundred.csv", mode='a', header=False, index = False)
