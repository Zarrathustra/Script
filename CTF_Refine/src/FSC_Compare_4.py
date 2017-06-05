from pylab import *
import numpy as np

import sys
import os

figure(figsize = (9, 6), dpi = 300)

lines_A = open(sys.argv[1]).readlines()
lines_B = open(sys.argv[2]).readlines()
lines_C = open(sys.argv[3]).readlines()
lines_D = open(sys.argv[4]).readlines()

X_A = [float(line.strip().split()[0]) for line in lines_A]
Y_A = [float(line.strip().split()[1]) for line in lines_A]
Z_A = [float(line.strip().split()[2]) for line in lines_A]

X_B = [float(line.strip().split()[0]) for line in lines_B]
Y_B = [float(line.strip().split()[1]) for line in lines_B]
Z_B = [float(line.strip().split()[2]) for line in lines_B]

X_C = [float(line.strip().split()[0]) for line in lines_C]
Y_C = [float(line.strip().split()[1]) for line in lines_C]
Z_C = [float(line.strip().split()[2]) for line in lines_C]

X_D = [float(line.strip().split()[0]) for line in lines_D]
Y_D = [float(line.strip().split()[1]) for line in lines_D]
Z_D = [float(line.strip().split()[2]) for line in lines_D]

plot(X_A, Z_A, label = sys.argv[7])
plot(X_B, Z_B, label = sys.argv[8])
plot(X_C, Z_C, label = sys.argv[9])
plot(X_D, Z_D, label = sys.argv[10])

plot(X_A, [0.5] * len(X_A), linestyle = 'dashed', c = 'green')
plot(X_A, [0.143] * len(X_A), linestyle = 'dashed', c = 'green')

xlabel(r'Spatial Frequency $\AA$')
ylabel('FSC')

xlim([0, X_A[-1]])
ylim([0, 1])

legend()

title(sys.argv[6])

tic = np.linspace(0, X_A[-2], num = 5)

xticks([int(x) for x in tic], ['{:.2f}'.format(Y_A[int(x)]) for x in tic])

savefig(sys.argv[5], dpi = 300)
