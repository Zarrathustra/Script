from pylab import *
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines();

THETA = [float(line.strip().split()[0]) for line in lines]
PDF_0 = [float(line.strip().split()[1]) for line in lines]
PDF_1 = [float(line.strip().split()[2]) for line in lines]
PDF_2 = [float(line.strip().split()[3]) for line in lines]
PDF_3 = [float(line.strip().split()[4]) for line in lines]
PDF_4 = [float(line.strip().split()[5]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

plot(THETA, PDF_0, label = "$\kappa = 0$")
plot(THETA, PDF_1, label = "$\kappa = 0.5$")
plot(THETA, PDF_2, label = "$\kappa = 1$")
plot(THETA, PDF_3, label = "$\kappa = 2$")
plot(THETA, PDF_4, label = "$\kappa = 4$")

xlabel("$\mu$")
ylabel("P")

xlim([-pi, pi])
ylim([0, 1])

xticks([-pi, -pi / 2, 0, pi / 2, pi], \
       ["$-\pi$", r"$-\frac{\pi}{2}$", 0, r"$\frac{\pi}{2}$", "$\pi$"])

title("Probabilty Density Function of von Mises Distribution")

legend()

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 500)
