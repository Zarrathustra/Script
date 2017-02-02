from pylab import *

filename = "../Data/MKB_FT_ORDER_0_3-8_10.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 5), dpi = 80)

plot(X, Y, linewidth = 2, alpha = 0.7)

xlim(0, 3.8)

title(r"Windowed Modified Kaiser Bessel Function, $a = 3.8, m = 0, \alpha = 10$")

savefig("../Figures/MKB_FT_ORDER_0_3-8_10.png", dpi = 200)
