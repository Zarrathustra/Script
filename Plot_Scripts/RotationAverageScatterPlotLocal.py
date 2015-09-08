from pylab import *

X = []
Y = []

lines = open("../Data/RotationAverage.txt", "r").readlines()

Y = [line.strip().split()[0] for line in lines]
X = range(size(Y))

figure(figsize = (10, 5), dpi = 500)

X = X[30:70]
Y = Y[30:70]

scatter(X, Y, c = "black", s = 5)
plot(X, Y)

plot([41.3, 41.3], [0, 1], linestyle = "-", linewidth = 2, c = "black")
plot([58.8, 58.8], [0, 1], linestyle = "-", linewidth = 2, c = "black")

fontSize = 10

annotate("1st zero point",
         xy = (41.3, 0),
         xycoords = "data",
         xytext = (15, 15),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

annotate("2nd zero point",
         xy = (58.8, 0),
         xycoords = "data",
         xytext = (15, 15),
         textcoords = "offset points",
         fontsize = fontSize,
         arrowprops = dict(arrowstyle = "->",
                           connectionstyle = "arc3"))

xlim(X[0], X[-1])
ylim(0, 1)

xlabel("Frequnecy")
ylabel("FRC")

title("Local Region of Rotation Average of an Ideal CTF with Astigmatism")

savefig("../Figures/RotationAverageCTFAstigmatismLocal.png", dpi = 200)
