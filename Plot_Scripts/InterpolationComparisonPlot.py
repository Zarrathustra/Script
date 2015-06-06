from pylab import *

X = []
Y = []

lines = open("../Data/Model_Nearest_FSC.csv", "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Model_Nearest = [line.strip().split(",")[1] for line in lines]

lines = open("../Data/Model_Linear_FSC.csv", "r").readlines();
Model_Linear = [line.strip().split(",")[1] for line in lines]

lines = open("../Data/Model_Sinc_FSC.csv", "r").readlines();
Model_Sinc = [line.strip().split(",")[1] for line in lines]

# lines = open("Nearest_Sinc_FSC.csv", "r").readlines();
# Nearest_Sinc= [line.strip().split(",")[1] for line in lines]

# lines = open("Linear_Sinc_FSC.csv", "r").readlines();
# Linear_Sinc= [line.strip().split(",")[1] for line in lines]

figure(figsize = (10, 5), dpi = 80)

lw = 4

plot(X, Model_Nearest, linewidth = lw, color = "green")
plot(X, Model_Linear, linewidth = lw + 2, color = "red")
plot(X, Model_Sinc, linewidth = lw - 1, color = "blue")
# plot(X, Linear_Sinc, linewidth = lw, color = "orange")
# plot(X, Nearest_Sinc, linewidth = lw, color = "yellow")

xlim(0, int(int(X[-1]) * 0.8))
ylim(0.5, 1)

savefig("../Figures/InterpolationComparisonPlot.png", dpi = 200)
show()
