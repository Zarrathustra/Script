# argument 1 : the filename of input data

import sys
import os
from pylab import *

filename = sys.argv[1]
inputFilename = "bar/" + filename
outputFilename = os.path.splitext(filename)[0] + ".png"

Y = []

lines = open(inputFilename, "r").readlines();

Y = [line.strip().split(",")[0] for line in lines]

Y.pop(0);

width = 0.5
X = [x + width / 2 for x in range(len(Y))]
Y = [int(y) for y in Y]

figure(figsize = (5, 3), dpi = 80)

bar(X, Y, hatch = "/", fill = False, width = width)
for x, y in zip(X, Y):
    text(x + 0.1, y + 0.5, str(y))

xlim(0, X[-1] + 1)
ylim(0, max(Y) * 1.1)

xTickPos = [x + width / 2 for x in X]
xticks(xTickPos, "")

savefig("result/" + outputFilename, dpi = 200)
