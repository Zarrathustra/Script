from pylab import *

import sys
import os

figure(figsize = (9, 6), dpi = 300)

lines_A = open(sys.argv[1]).readlines()
lines_B = open(sys.argv[2]).readlines()

X_A = [float(line.strip().split()[0]) for line in lines_A]
Y_A = [float(line.strip().split()[2]) for line in lines_A]
Z_A = [float(line.strip().split()[4]) for line in lines_A]

X_B = [float(line.strip().split()[0]) for line in lines_B]
Y_B = [float(line.strip().split()[1]) for line in lines_B]
Z_B = [float(line.strip().split()[2]) for line in lines_B]

plot(X_A, Z_A, label = sys.argv[4])
plot(X_B, Z_B, label = sys.argv[5])

plot(X_A, [0.5] * len(X_A), linestyle = 'dashed', c = 'green')
plot(X_A, [0.143] * len(X_A), linestyle = 'dashed', c = 'green')

xlabel('Resolution')
ylabel('FSC')

xlim([0, X_A[len(X_A) - 1]])
ylim([0, 1])

legend()

title(sys.argv[6])

savefig(sys.argv[3], dpi = 300)
