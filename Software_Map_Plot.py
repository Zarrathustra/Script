import sys
from pylab import *

filename = "Software_Map.csv"

# Data Reading and Cleaning
lines = open(filename, "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Y = [line.strip().split(",")[1] for line in lines]
X.pop(0)
Y.pop(0)
Y = [int(y) for y in Y]

figure(figsize = (5, 5), dpi = 80)

explode = [0.05 for i in range(len(X))]
pie(Y, labels = X, explode = explode)


savefig("Software_Map.png", dpi = 200)
show()
