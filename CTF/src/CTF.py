from pylab import *

import sys
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

filename = os.path.splitext(filename)[-2]
filename = filename.split('/')[-1]

figure(figsize = (10, 5), dpi = 300)

plot(X, Y, linewidth = 2, alpha = 0.7)

xlabel('Spatial Frequency')
ylabel('CTF')

savefig("../Figures/" + filename + ".png", dpi = 300)
