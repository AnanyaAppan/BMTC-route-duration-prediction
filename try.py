from os import listdir
from os.path import isfile, join


onlyfiles = [f.strip()[:-4] for f in listdir("/home/ananya/Documents/BMTC/final/") if isfile(join("/home/ananya/Documents/BMTC/final/", f))]
onlyfiles.sort()
files = map(int,onlyfiles)
print(files)