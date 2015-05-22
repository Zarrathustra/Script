import sys
from pylab import *

filename = "Software_Map_HighResolution.csv"

# Data Reading and Cleaning
lines = open(filename, "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Y = [line.strip().split(",")[1] for line in lines]
X.pop(0)
Y.pop(0)
Y = [int(y) for y in Y]

def my_autopct(pct):
    total = sum(Y)
    val = int(pct * total / 100.0)
    return "{v:d}".format(v = val)

figure(figsize = (5, 5), dpi = 80)

explode = [0.05 for i in range(len(X))]
pie(Y, labels = X, explode = explode, autopct = my_autopct)

title(r"EM Density Maps at the Resolution above $4\AA$")

savefig("Software_Map_HighResolution.png", dpi = 200)
show()
