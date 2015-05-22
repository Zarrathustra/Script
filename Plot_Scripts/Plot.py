# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel
# argument 4 : the filename of output image

import sys
from pylab import *

filename = sys.argv[1]

X = []
Y = []

lines = open(filename, "r").readlines();

X = [line.strip().split()[0] for line in lines]
Y = [line.strip().split()[1] for line in lines]

figure(figsize = (10, 5), dpi = 80)
# subplot(1, 1, 1)
# axes([0.025, 0.025, 0.95, 0.95])

colors = [float(y) for y in Y]

plot(X, Y, linewidth = 2, alpha = 0.7)

xlim(0, int(X[-1]))
ylim(-1, 1)

xlabel(sys.argv[2])
ylabel(sys.argv[3])

savefig(sys.argv[4], dpi = 200)
show()
