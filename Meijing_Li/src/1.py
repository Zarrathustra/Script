import os
import sys

lines = open("../Data/refine.star", "r").readlines()

coordX = [float(line.strip().split()[10]) for line in lines]
coordY = [float(line.strip().split()[11]) for line in lines]

transX = [float(line.strip().split()[15]) for line in lines]
transY = [float(line.strip().split()[16]) for line in lines]

names = [line.strip().split()[13] for line in lines]
nameSet = set(names)

names = [os.path.splitext((os.path.split(name)[-1]))[0] for name in names]

os.system("rm -f ../Result/*.star")

l = len(lines)
for i in range(l):
    print str(i) + "/" + str(l)
    file = open("../Result/" + names[i] + ".star", 'a')
    file.write(str(coordX[i] + transX[i]) + " " + str(coordY[i] + transY[i]) + "\n")
    file.close()
