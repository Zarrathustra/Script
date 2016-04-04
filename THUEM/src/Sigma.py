from pylab import *
import math

N = 13

X = []

for i in range(N):
    F = open("../Data/Sigma/Sigma_0" + str(i) + ".txt", "r")
    X.append(F.readline().split()[:-1])
    X[i] = [math.log(float(x)) for x in X[i]]

figure(figsize = (10, 10), dpi = 500)

for i in range(N):
    plot(range(len(X[i])), X[i], label = r"$\sigma$, Round " + str(i))

legend()

xlabel("Spatial Frequency")
ylabel(r"$\log\sigma$")

savefig("../Figures/Sigma.png", dpi = 500)
