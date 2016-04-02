from pylab import *
import math

F = open("../Data/Sigma/Sigma_00.txt", "r")
X0 = F.readline().split()[:-1]
X0 = [math.log(float(x)) for x in X0]
F = open("../Data/Sigma/Sigma_01.txt", "r")
X1 = F.readline().split()[:-1]
X1 = [math.log(float(x)) for x in X1]

figure(figsize = (10, 10), dpi = 500)

plot(range(len(X0)), X0, c = "b", label = r"$\sigma$, Round 0")
plot(range(len(X1)), X1, c = "g", label = r"$\sigma$, Round 1")

legend()

xlabel("Spatial Frequency")
ylabel(r"$\log\sigma$")

savefig("../Figures/Sigma.png", dpi = 500)
