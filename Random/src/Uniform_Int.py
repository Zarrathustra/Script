from pylab import *

filename = "../Data/Uniform_Int.txt"

lines = open(filename, "r").readlines();

K = 10

X = [int(line.strip().split()[0]) for line in lines]
Y = [int(line.strip().split()[1]) for line in lines]
W = [float(line.strip().split()[2]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

scatter(X, Y, s = [50 * K * K * w for w in W], \
        alpha = 0.8, \
        linewidth = 0, \
        color = "green")

xlim([-1, K])
ylim([-1, K])

xticks(range(0, K), range(0, K))
yticks(range(0, K), range(0, K))

title("2D Discrete Uniform Distribution")

savefig("../Figures/Uniform_Int.png", dpi = 500)
