from pylab import *

lines = open("../Data/Spectrum.txt", "r").readlines()

X = lines[0].split(' ')
X.pop(-1)

X = [log(float(x)) for x in X]

figure(figsize = (10, 5), dpi = 200)

plot(range(len(X)), X)

xlabel("frequency in pixel")
ylabel("logarithm of intensity")

title("Power Spectrum")

savefig("../Figures/Spectrum.png", dpi = 200)
