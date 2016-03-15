from pylab import *

filename = "No_Header.star"

lines = open(filename, "r").readlines();

# print lines[0].strip().split()[17]

Group = [int(line.strip().split()[14]) for line in lines]
MicID = [int((line.strip().split()[13])[15:19]) for line in lines]

for i in range(len(lines)):
    print Group[i], MicID[i]
