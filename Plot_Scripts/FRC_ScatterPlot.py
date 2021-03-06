# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel
# argument 4 : the title

import os
import sys
from pylab import *

filename = sys.argv[1]

X = []
Y = []

lines = open(filename, "r").readlines();

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

X = [float(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 800)

scatter(X, Y, linewidth = 1, marker = u'+');

xlim(0, 1000)
ylim(0, 1)

xlabel(sys.argv[2])
ylabel(sys.argv[3])

title(sys.argv[4])

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 800)
