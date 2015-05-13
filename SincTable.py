# generate a normalized sinc function value table

import math
from pylab import *

N = 1000

sincTable = open("SincTable.txt", "w", -1)

sincTable.write("1" + ",\n")

value = [1]

for i in range(1, N):
    par = math.pi * i / N
    value.append(math.sin(par) / (par))
    sincTable.write(str(value[i]) + ",\n")

X = range(N)

figure(figsize = (10, 5), dpi = 80)

plot(X, value)

savefig("SincTable.png", dpi = 200)
show()
