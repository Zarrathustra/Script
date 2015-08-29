from pylab import *

X = []
Y = []

lines = open("../Data/RotationAverage.txt", "r").readlines();

Y = [line.strip().split()[0] for line in lines]
X = range(size(Y))

figure(figsize = (10, 5), dpi = 500)

scatter(X, Y, c = "black", s = 5)
plot(X, Y)

xlim(0, size(Y))
ylim(0, 1)

title("Rotation Average of an Ideal CTF with Astigmatism")

savefig("../Figures/RotationAverageCTFAstigmatism.png", dpi = 200)
