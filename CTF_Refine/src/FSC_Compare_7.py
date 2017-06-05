from pylab import *
import numpy as np

import sys
import os

figure(figsize = (9, 6), dpi = 300)

for i in range(7):
    global X, Y, Z

    lines = open(sys.argv[1 + i]).readlines()

    X = [float(line.strip().split()[0]) for line in lines]
    Y = [float(line.strip().split()[1]) for line in lines]
    Z = [float(line.strip().split()[2]) for line in lines]

    plot(X, Z, label = sys.argv[10 + i])

plot(X, [0.5] * len(X), linestyle = 'dashed', c = 'green')
plot(X, [0.143] * len(X), linestyle = 'dashed', c = 'green')

xlabel(r'Spatial Frequency $\AA$')
ylabel('FSC')

xlim([0, X[-1]])
ylim([0, 1])

legend()

title(sys.argv[9])

tic = np.linspace(0, X[-2], num = 5)

xticks([int(x) for x in tic], ['{:.2f}'.format(Y[int(x)]) for x in tic])

savefig(sys.argv[8], dpi = 300)
