# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel

import os
import sys
from pylab import *

filename = sys.argv[1]

X = []
Y = []

lines = open(filename, "r").readlines();

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

X.pop(0)
Y.pop(0)

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 200)

colors = [float(y) for y in Y]

scatter(X, Y, c = colors, s = 20, alpha = 0.5)

xlim(0, int(X[-1]))
ylim(0, 1)

xlabel(sys.argv[2])
ylabel(sys.argv[3])

basename = os.path.basename(filename)

savefig("../Figures/" + basename + ".png", dpi = 200)
