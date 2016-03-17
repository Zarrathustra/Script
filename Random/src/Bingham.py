from pylab import *
import os

N = 100000

filename = sys.argv[1]

lines = open(filename, "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (20, 10), dpi = 500)

scatter(X[:N], Y[:N], alpha = 0.1,
        linewidth = 0, color = "black")

xlim(-0.5, 2 * pi + 0.5)
ylim(-0.5, pi + 0.5)

xticks([0, pi, 2 * pi], ["0", r"$\pi$", r"$2\pi$"])
yticks([0, pi], ["0", r"$\pi$"])

xlabel(r"$\phi$")
ylabel(r"$\theta$")

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 500)
