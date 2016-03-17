from pylab import *

filename = "../Data/Tab_MKB_FT_2_15.txt"

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 5), dpi = 500)

plot(X, Y, linewidth = 2, alpha = 0.7)

xlim(0, 1.5)

title(r"Windowed Modified Kaiser Bessel Function Using TabFunction, $m = 2, \alpha = 15$")

savefig("../Figures/Tab_MKB_FT.png", dpi = 500)
