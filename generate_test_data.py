import pandas as pd
import csv
import random 

busId = [150218622, 150219820, 150814442, 150221816, 150221298, 150221295, 150222058, 150219884, 150220607, 150813618, 150218085, 150812912, 150222113, 150219731, 150811567, 150811277, 150222320, 150222076, 150218225, 150220276, 150222876, 150219058, 150222690, 150222938, 150221304, 150219042, 150221435, 150811366, 150218960, 150219903, 150810490, 150221099, 150222606, 150222406, 150813920, 150218576, 150222082, 150814482, 150218092, 150814725, 150220081, 150218902, 150220220, 150219162, 150222045, 150218456, 150220069, 150221720, 150220322, 150222810, 150218181, 150219120, 150812841, 150222708, 150220199, 150222971, 150220198, 150813833, 150222474, 150220548]

with open('test_data.csv', 'a') as csvFile:
    fieldnames = ['BusId', 'TimeStamp']
    latLongfieldnames = ['LATLONG'+str(var) for var in range(1,101)]
    fieldnames = fieldnames + latLongfieldnames + ['PredTimeSec']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    rowDict = dict()

    for bus in busId:
        lat_long_count = 1
        travel_time = 0
        prev_time = 0
        rowDict['BusId'] = bus

        for chunk in pd.read_csv("encoded_hundred.csv", names = ["index","busId" , "latitude", "longitude", "angle", "speed", "timestamp", "gridNum", "time", "day"], chunksize = chunksize):

            df = pd.DataFrame(chunk)

            if lat_long_count == 101:
                rowDict['PredTimeSec'] = travel_time
                writer.writerow(rowDict)
                break

            for var in range(len(df)):
                pick_point = (random.randint(0,20))%2

                if lat_long_count == 101:
                    break
                if(df.loc[var, "busId"] == bus and pick_point):
                    if(lat_long_count == 1):
                        rowDict['TimeStamp'] = df.loc[var, "timestamp"]
                    rowDict['LATLONG'+str(lat_long_count)] = df.loc[var, "latitude"] + ":" + df.loc[var, "longitude"]
                    travel_time = df.loc[var, "time"]*60 - prev_time
                    prev_time = df.loc[var, "time"]*60
                    lat_long_count += 1

                else:
                    temp_df = pd.DataFrame(df.loc[var]).T
                    temp_df.to_csv('lalliTrial/train_hundred.csv', mode='a', header=False, index = False)
