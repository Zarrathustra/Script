# argument 1 : the filename of input data

import sys
import os
from pylab import *

inputFilename = sys.argv[1]
outputFilename = os.path.splitext(inputFilename)[0] + ".png"

X = []
Y = []

lines = open(inputFilename, "r").readlines();

X = [line.strip().split(",")[0] for line in lines]
Y = [line.strip().split(",")[1] for line in lines]

X.pop(0);
Y.pop(0);

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (5, 3), dpi = 80)

plot(X, Y, linewidth = 2, c = "k")

xlim(0, int(X[-1]))

savefig("result/" + outputFilename, dpi = 200)
