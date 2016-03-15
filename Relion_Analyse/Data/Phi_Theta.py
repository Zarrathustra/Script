from pylab import *

filename = "No_Header.star"

lines = open(filename, "r").readlines();

# print lines[0].strip().split()[17]

Phi = [float(line.strip().split()[17]) for line in lines]
Theta = [float(line.strip().split()[18]) for line in lines]

for i in range(len(lines)):
    print Phi[i], Theta[i]
