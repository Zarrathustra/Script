# argument 1 : the filename of input data

import sys
import os
from pylab import *

inputFilename = sys.argv[1]
outputFilename = os.path.splitext(inputFilename)[0] + ".png"

X = []
Y1 = []
Y2 = []

lines = open(inputFilename, "r").readlines();

X = [line.strip().split(",")[0] for line in lines]
Y1 = [line.strip().split(",")[1] for line in lines]
Y2 = [line.strip().split(",")[2] for line in lines]

X.pop(0);
Y1.pop(0);
Y2.pop(0);

X = [float(x) for x in X]
Y1 = [float(y) for y in Y1]
Y2 = [float(y) for y in Y2]

figure(figsize = (5, 3), dpi = 80)

plot(X, Y1, linewidth = 2, c = "r")
plot(X, Y2, linewidth = 2, c = "b")

xlim(0, int(X[-1]))

savefig("result/" + outputFilename, dpi = 200)
