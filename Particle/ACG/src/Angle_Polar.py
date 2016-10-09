from pylab import *
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines()

PHI = [float(line.strip().split()[0]) for line in lines]
THETA = [float(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

subplot(111, projection = 'polar')

c = scatter(PHI, THETA, c = "black", linewidth = 0)
c.set_alpha(0.1)

ylim([0, pi])
yticks([0, pi / 4, pi / 2, pi / 4 * 3, pi],
       [0,
        r"$\frac{\pi}{4}$",
        r"$\frac{\pi}{2}$",
        r"$\frac{3\pi}{4}$",
        r"$\pi$"])

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + "_Polar.png", dpi = 500)
