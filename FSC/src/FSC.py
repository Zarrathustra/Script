from pylab import *

import sys
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]
Z = [float(line.strip().split()[2]) for line in lines]

filename = os.path.splitext(filename)[-2]
filename = filename.split('/')[-1]

figure(figsize = (10, 5), dpi = 300)

plot(X, Z, linewidth = 2, alpha = 0.7)

plot(X, [0.143 for x in X], linestyle = 'dashed')

plot(X, [0.5 for x in X], linestyle = 'dashed')

xticks([30, 60, 90, 120, 150, 180],
       [Y[50], Y[60], Y[90], Y[120], Y[150], Y[180]])

#xlim(0, 1.5)

#title(r"Windowed Modified Kaiser Bessel Function, $m = 2, \alpha = 0.5$")

#savefig("../Figures/MKB_FT.png", dpi = 200)

savefig("../Figures/" + filename + ".png", dpi = 300)
