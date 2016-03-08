from pylab import *

filename = "../Data/MKB_FT_2_5.txt"
lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y_1 = [float(line.strip().split()[1]) for line in lines]

filename = "../Data/MKB_FT_2_10.txt"
lines = open(filename, "r").readlines();

Y_2 = [float(line.strip().split()[1]) for line in lines]

filename = "../Data/MKB_FT_2_15.txt"
lines = open(filename, "r").readlines();

Y_3 = [float(line.strip().split()[1]) for line in lines]

filename = "../Data/MKB_FT_2_20.txt"
lines = open(filename, "r").readlines();

Y_4 = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 5), dpi = 500)

plot(X, Y_1, linewidth = 2, alpha = 0.7, color = "blue", \
     label = r"$a = 2, \alpha = 5$")
plot(X, Y_2, linewidth = 2, alpha = 0.7, color = "green", \
     label = r"$a = 2, \alpha = 10$")
plot(X, Y_3, linewidth = 2, alpha = 0.7, color = "orange", \
     label = r"$a = 2, \alpha = 15$")
plot(X, Y_4, linewidth = 2, alpha = 0.7, color = "red", \
     label = r"$a = 2, \alpha = 20$")

legend()

xlim(0, 2.5)

title(r"Windowed Modified Kaiser Bessel Function, $m = 2$")

savefig("../Figures/MKB_FT_Compare.png", dpi = 500)
