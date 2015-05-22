# argument 1 : the filename of input data

import sys
import os
from pylab import *

filename = sys.argv[1]

X = []
Y = []

lines = open(filename, "r").readlines();
close(filename)

X = [line.strip().split(",")[0] for line in lines]
Y = [line.strip().split(",")[1] for line in lines]

X.pop(0);
Y.pop(0);

X = [float(x) for x in X]
Y = [-float(y) for y in Y]

out = open(filename, "w")
for i in range(len(X)):
    out.writelines(str(X[i]) + "," + str(Y[i]) + "\n")
