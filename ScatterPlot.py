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

scatter(X, Y, c = colors, s = 15, alpha = 0.5)

xlim(0, int(X[-1]))
ylim(0, 1)

xlabel(sys.argv[1])
ylabel(sys.argv[2])

# savefig("FRCout.bmp", dpi = 200)
show()
