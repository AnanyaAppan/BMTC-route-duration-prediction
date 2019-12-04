import math
import sys
from encode_data import encode_weekday
from encode_data import encode_time
from get_grid import get_grid
from get_grid import sub_grid
from datetime import datetime
from datetime import timedelta
import pandas as pd


files = [541, 1653, 741, -1031, 73, 646, 277, 2230, 1280, 1002, 1136, 511, -78, 1147, 994, 215, 470, 756, -146, -674, 187, 760, 378, 656, 965, 788, 391, 652, 737, 1162, 1971, 1243, 721, -316, 1423, 871, 1621, 1463, 1466, 819, 1462, 647, 178, 1161, 418, 2197, 998, 502, 787, 518, 467, 1333, -39, 830, 898, -452, 1107, 989, 911, 194, 897, 326, 1338, 734, 2155, 526, -181, 1201, 451, 290, 568, 1551, 1103, 655, 1141, 424, 184, 1034, 924, 122, 1766, 719, 1131, 363, 1045, 1308, 705, 642, 875, 1339, 212, 2191, 180, 1203, 1016, 1556, 588, 935, 1332, 701, 559, -789, 147, 736, 619, 151, 597, 428, 708, 1757, 1044, 316, 1138, -396, 970, 2138, 1030, 1102, 1122, 1077, 1373, 846, 242, 450, 637, 121, 1120, 416, 244, 1246, 648, 1017, 261, 535, 1062, 347, 192, 1277, 624, -722, 420, 1137, 592, 2126, -858, 216, 852, 753, 544, 636, 516, -536, 1370, 960, 786, 1345, 351, 1164, 113, 759, 1622, -681, 1426, 1457, 449, 1130, 956, 444, 770, 214, 225, 496, 1250, 2026, 1057, -362, 729, 918, 1275, 319, 1732, 555, -520, 2059, -856, -572, 415, 1205, 651, 185, 1232, 1937, 611, 943, 308, 731, 676, 1522, 1168, 353, -1384, 532, 294, 493, 1589, 767, 255, 426, 1800, 1190, 1179, -1372, 671, 1111, -676, 818, 843, 969, 485, 530, 1271, 1041, 801, 1304, 904, 43, 2227, 1657, 870, 1059, 954, 462, -963, -1381, 465, 980, 828, 1035, 802, 942, -1373, -574, 307, 1306, 1283, 2192, 355, -687, 494, 357, 548, -553, 743, 1149, -112, 860, 805, 804, 995, 2198, 1284, -75, 644, 321, 618, 1422, 413, 2261, 657, 1146, 1199, 1144, 773, 136, 1215, 361, -928, 461, 740, 464, 893, 348, 717, 329, -646, 67, 1903, 156, 455, 829, 477, 114, 1091, 226, 324, 758, 328, 563, 974, 1060, 2262, 738, 206, 662, 488, 2157, 1400, 1310, 722, -610, 514, 742, 1467, 1152, 620, 158, -715, 1733, 955, 836, 1140, 108, 586, 522, 1000, 1079, 892, -680, 835, 673, 1003, 190, 1183, 975, 856, 1598, 149, 761, -685, 1483, 1631, 75, 153, 1453, 810, 422, 832, 629, 181, 1008, 744, 650, 929, 423, 1212, 849, 515, 274, 1233, 776, 1925, 1172, 895, 175, 1211, -290, 1756, 585, 703, 1082, 851, 110, 692, 1464, 1176, 211, 8, 1067, 919, 342, -326, 612, 693, 310, 587, 88, 433, 691, 281, 1654, 438, 1029, 614, 792, 979, 359, 914, 755, 320, 141, 699, 503, 959, 495, 397, 224, 1248, 102, 1488, 208, 869, -997, 1032, -77, 1456, -684, 1039, 443, 928, 150, 1665, 528, 1143, 626, -721, 383, -571, 889, 1096, 48, -41, 573, 1015, -4, 119, 2229, 454, 688, 1047, 913, 1132, 748, 286, 682, -655, -291, 785, -252, -538, 362, 9, 425, -787, 33, 1173, 501, 891, 393, 364, 1031, -418, 1377, 1133, 1959, -549, 466, 498, -537, 921, 463, 525, 20, 1531, 953, -584, 1171, 825, 330, 1314, 107, 1213, 1857, 85, 76, 360, 396, 1349, 625, 809, 1202, -718, 1139, -617, 1210, 654, 429, -606, 865, -620, -645, 1033, 1116, 1089, 689, 900, 962, 311, 1384, 376, 907, 561, 356, -3, -249, 220, 1097, 245, -826, 276, 421, 243, 1104, 749, 752, 546, 2196, 595, 1351, 850, 285, 880, 315, 157, 570, 1231, 253, 284, 148, -288, 1004, 562, -723, 504, 1040, 278, 314, -791, 2226, 2165, 879, 414, 5, -76, 1010, 750, 1459, 866, 1024, 2038, 997, 991, 934, 589, 560, 1128, 317, 550, 457, 857, 1235, 582, -26, 1005, 82, 716, 1177, 74, 247, 1313, 517, 833, 1269, 545, -1406, 763, 172, -689, -350, 483, 313, 481, 1023, -217, 1098, 1318, 945, 500, 1110, 992, 864, 751, 572, 967, 1481, 937, 1197, 1088, 1073, 146, 209, 564, -753, 1012, 1272, 2163, 1150, 1790, 254, 1249, -1383, -183, 1126, 480, 1106, 927, 218, 1265, 1586, -384, 1151, 273, 1656, 412, 901, 1075, 621, 847, 191, 1824, 784, 931, 1051, -1379, 903, 482, 499, 700, 1166, 596, 1279, 440, -754, 124, 867, 1690, 1090, 1156, -289, 578, 1419, 1305, 1238, 820, 1175, 431, 345, 1145, -397, 1234, 2194, 1427, 601, 279, 1013, 1208, 591, 478, 1209, 507, 510, 1063, 394, 2228, 1244, 1380, 862, -857, 1070, 888, -2, 486, 430, -822, 660, 667, 1869, 668, 1597, 1458, 460, 1105, 520, 882, 631, 537, 806, 841, -27, 417, 1270, 32, 248, 557, 176, 340, 583, 976, 1158, 941, 1038, 2087, 1415, -361, 111, 823, 827, 593, -360, 1342, -575, 1074, 524, 821, -468, 1379, 754, 1298, 1169, 1195, 411, 664, 322, 445, 379, 1207, 632, 2132, 772, 697, 473, -1389, 508, 635, 1181, 154, 1095, 395, 250, 1433, 283, 685, 280, 174, 1311, 553, -587, 542, 2135, 718, 1413, 638, 1240, 639, 1049, 1336, -825, 764, 472, 1425, 1835, 1189, 534, 853, 1157, -686, 565, 677, 640, -745, -283, 1001, 1242, 707, 492, 1858, 182, 909, -253, 577, -859, 1148, 765, 1180, 628, 252, -644, 1055, 910, 842, 798, 1028, 981, 622, 1335, 567, 674, 858, -678, 523, 1303, -466, 219, 704, 774, 714, -1378, 539, 1081, 1346, 600, 694, 1108, 380, -716, 876, 1101, 293, 1239, 1315, 505, 1027, -711, 793, 961, -688, 1094, 177, 2106, -147, 1178, -894, 1042, 381, 1129, 822, 1264, -621, 1163, -1375, 848, 1006, 1153, 179, 1182, 1565, 993, 227, 2121, 531, 223, 605, 723, 1801, 733, 1068, -654, 727, 933, 940, 1174, 1118, 291, 824, -788, 1282, 837, 287, 873, 957, 341, 207, 906, 768, 996, 289, 387, 1076, 452, -757, 932, -893, 2156, 686, 964, -38, 881, 968, 1487, 189, -486, 613, 579, 476, 794, -860, 1025, -554, 1124, 469, 899, 2139, 1245, 630, 1009, 427, 590, 529, 777, 1623, -215, 354, 800, 193, 576, 775, 1135, 1274, 771, 728, 2025, 487, 171, 2199, 442, 432, 720, 552, 1078, 390, 769, 715, 1517, 698, 617, 1334, 447, -717, 799, 690, 971, 1167, 725, 137, 1026, 446, 571, -679, -467, 838, 468, 603, 1119, -282, -63, 584, 145, 1154, 990, 344, 1347, 349, -651, 1348, 890, 2137, 839, 246, 1064, 633, 77, 2134, 210, 920, 260, 1371, 812, -218, 706, 1115, 615, 739, 1216, -677, 2166, 142, 521, 221, 556, 606, -618, 1007, 484, 999, 1050, 318, 439, -755, 258, 840, 1312, 1278, 306, 288, 256, 1185, 1184, 905, -1377, 649, 533, 683, 1699, 87, 966, 886, 1455, 902, 115, 123, 608, 2133, 762, 116, 963, 323, 887, 1428, 343, 458, 2088, 325, 1723, -432, 1465, 663, 490, 188, 1489, 2092, 861, 643, -1374, 1276, 807, -640, 312, 282, 489, 1992, 358, -182, 1958, 448, 375, 1599, 1620, 42, 594, -583, 346, -1390, 527, 1046, 946, 453, 569, 1424, 1585, 491, 296, 1056, -40, 831, 666, 109, 292, 602, 2072, 859, 186, 896, 1066, 1214, 1061, -1376, -325, 874, 735, 1497, 1372, 1204, -962, 1317, 249, 661, 456, 1268, 783, 665, 228, 1206, 938, 1112, -1380, -573, 81, 936, 1113, 1036, 868, 811, 1069, 978, 1100, 68, 789, 350, 925, 616, 554, 944, -779, -180, 1399, -675, 79, 580, 222, 144, 791, 1366, 1170, 1080, 684, 497, 1109, 863, 384, 566, 687, 658, 549, -29, 627, 1590, -1382, 382, 854, 796, 2136, 1350, 1891, 1134, 2105, -539, 389, 877, 696, 2093, 659, 926, 977, 1083, 878, 1114, 634, 39, 2005, 726, 790, 834, 120, 7, 257, -502, 610, 295, 1447, 459, 1065, 479, 604, 112, 1198, 14, 1043, 908, 795, 803, 1385, 385, 1071, 2004, 386, 845, 1241, 327, 930, 669, 1236, 923, 1381, 732, -752, 599, 855, -254, 653, 702, 1309, 1072, 1237, 645, 410, 724, 392, 1316, 1084, 1229, 695, 1037, 1022, 680, 670, 2160, 1302, 872, 558, 419, 1449, 117, 679, 766, 1093, 797, 1099, 672, 1343, 54, 826, 1127, 388, 894, 922, 259, 939, 710, 1142, 952, 352, 1125, 519, 947, 757, 143, 623, 506, 598, 1281, -609, 213, 155, 730]

filename = "/home/ananya/Documents/BMTC/final/fitted_final_grouped.csv"

chunksize = 10**5

lat = 12.66 
long = 77.27 

length_lat = 0.032/2
length_long = 0.043/2

def get_row(grid_num):
    return grid_num/34

def get_col(grid_num):
    return grid_num % 34

def grid_dist(grid1,grid2):
    row1 = get_row(grid1)
    row2 = get_row(grid2)
    col1 = get_col(grid1)
    col2 = get_col(grid2)
    return abs(row1-row2) + abs(col1-col2)

def closest_col(col1, col2):
    return pd.Series.abs(col1-col2)

def get_lat_lon_dist(lat1,lon1,lat2,lon2):
    radius = 6371
    dLat = (math.pi/180)*(lat2-lat1)
    dLon = (math.pi/180)*(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos((math.pi/180)*(lat1)) * math.cos((math.pi/180)*(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # distance in km
    distance = radius * c
    return distance

def get_time(lat1, lon1, lat2, lon2, timestamp):
    
    grid1 = get_grid(lat1, lon1)
    grid2 = get_grid(lat2, lon2)
    sub_grid1 = sub_grid(lat1, lon1)
    sub_grid2 = sub_grid(lat2, lon2)
    day = encode_weekday(timestamp)
    time = encode_time(timestamp)
    distance = get_lat_lon_dist(lat1,lon1,lat2,lon2)
    closest_grid1 = int(min(files, key=lambda x:grid_dist(x,grid1)))
    closest_grid2 = int(min(files, key=lambda x:grid_dist(x,grid2)))

    filename1 = "/home/ananya/Documents/BMTC/final/"+str(closest_grid1)+".csv"
    filename2 = "/home/ananya/Documents/BMTC/final/"+str(closest_grid2)+".csv"

    speed1 = 0
    speed2 = 0

    # print("grid1 = ",grid1, " closest grid = ", closest_grid1)
    # print("grid2 = ",grid2, " closest grid = ", closest_grid2)

    for chunk in pd.read_csv(filename1,header=None,names = ["index","grid","subgrid","day","time","speed"], chunksize=chunksize):
        
        df = pd.DataFrame(chunk)
        df.insert(6,"abs_subgrid",closest_col(df.subgrid,sub_grid1))
        df.insert(7,"abs_day",closest_col(df.day,day))
        df.insert(8,"abs_time",closest_col(df.time,time))
        df = df.sort_values(["abs_subgrid","abs_day","abs_time"])
        # print(df.head())
        speed1 = df.iloc[0].speed
        # if(speed1 == 0): speed1 = df.groupby(["abs_subgrid","abs_day",pd.to_numeric(df.time/60, downcast='integer')])["speed"].mean().iloc[0]
        # if(speed1 == 0): speed1 = df.groupby(["abs_subgrid","abs_day"])["speed"].mean().iloc[0]
        if(speed1 == 0): speed1 = df.groupby("abs_subgrid")["speed"].mean().iloc[0]
        # print("speed1 =", speed1)

    for chunk in pd.read_csv(filename2,header=None,names = ["index","grid","subgrid","day","time","speed"], chunksize=chunksize):
        
        df = pd.DataFrame(chunk)
        df.insert(6,"abs_subgrid",closest_col(df.subgrid,sub_grid2))
        df.insert(7,"abs_day",closest_col(df.day,day))
        df.insert(8,"abs_time",closest_col(df.time,time))
        df = df.sort_values(["abs_subgrid","abs_day","abs_time"])
        # print(df.head())
        speed2 = df.iloc[0].speed
        # if(speed2 == 0): speed2 = df.groupby(["abs_subgrid","abs_day",pd.to_numeric(df.time/60, downcast='integer')])["speed"].mean().iloc[0]
        # if(speed2 == 0): speed2 = df.groupby(["abs_subgrid","abs_day"])["speed"].mean().iloc[0]
        if(speed2 == 0): speed2 = df.groupby("abs_subgrid")["speed"].mean().iloc[0]
        # print("speed2 =", speed1)

    # print("distance = ",distance)
    
    avg_speed = (speed1 + speed2)/2
    if(avg_speed == 0): avg_speed = 0.01
    # if(avg_speed == 0): avg_speed = 10
    # time in seconds
    if(distance==0): distance = 0.01
    time = (distance/avg_speed)*3600 
    print("time = ",time)
    return time

def increment_timestamp(time, timestamp):
    # print("time = ",time)
    # print("timestamp = ",timestamp)
    datetimeObj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return str(datetimeObj + timedelta(seconds = int(time)))

def get_total_time(lat_long, timestamp):
    time = 0
    for i in range(len(lat_long)-1):
        lat1, lon1 = map(float, lat_long[i].split(":"))
        lat2, lon2 = map(float, lat_long[i+1].split(":"))
        temp_time = get_time(lat1, lon1, lat2, lon2, timestamp)
        time += temp_time
        timestamp = increment_timestamp(temp_time, timestamp)
    return time,timestamp

def get_intermediate_nodes(l):
    l_new = []
    for i in range(1,len(l)):
        lat1,lon1 = map(float, l[i-1].split(":"))
        l_new.append(str(lat1)+":"+str(lon1))
        lat2,lon2 = map(float, l[i].split(":"))
        d = get_lat_lon_dist(lat1,lon1,lat2,lon2)
        if(d > 0.125): 
            m = 0.125
            while(m<d):
                x = m
                y = d-m
                lat_new = (x*lat2 + y*lat1)/(x+y)
                lon_new = (x*lon1 + y*lon2)/(x+y)
                l_new.append(str(lat_new)+":"+str(lon_new))
                m += 0.125
    l_new.append(l[len(l)-1])
    # print(l_new)
    return l_new



# increment_timestamp(345.78,'2016-07-01 00:06:10')
for chunk in pd.read_csv('/home/ananya/Documents/BMTC/final_bmtc_test_data.csv', header=None, chunksize=chunksize,skiprows=1):
    df = pd.DataFrame(chunk)
    for i in range(len(df)):
        row = df.iloc[i].values
        bus_id = row[0]
        timestamp = row[1].strip()
        lat_long = get_intermediate_nodes(row[2:])
        get_intermediate_nodes(lat_long)
        f_time,f_timestamp = get_total_time(lat_long, timestamp)
        data = {"bus_id" : [bus_id], "time" : [f_time]}
        df_new = pd.DataFrame(data)
        df_new.to_csv("/home/ananya/Documents/BMTC/final/bigFiles/test_final_7.csv",header=False, index=False,mode='a')





    