from pylab import *
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines();

VMS_0 = array([float(line.strip().split()[0]) for line in lines])
VMS_1 = array([float(line.strip().split()[1]) for line in lines])
VMS_2 = array([float(line.strip().split()[2]) for line in lines])
VMS_3 = array([float(line.strip().split()[3]) for line in lines])
VMS_4 = array([float(line.strip().split()[4]) for line in lines])
VMS_5 = array([float(line.strip().split()[5]) for line in lines])
VMS_6 = array([float(line.strip().split()[6]) for line in lines])
VMS_7 = array([float(line.strip().split()[7]) for line in lines])

figure(figsize = (10, 10), dpi = 500)

scatter(cos(VMS_0), sin(VMS_0), \
        color = "red", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 0$")
scatter(2 * cos(VMS_1), 2 * sin(VMS_1), \
        color = "orange", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 0.5$")
scatter(3 * cos(VMS_2), 3 * sin(VMS_2), \
        color = "yellow", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 1$")
scatter(4 * cos(VMS_3), 4 * sin(VMS_3), \
        color = "green", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 2$")
scatter(5 * cos(VMS_4), 5 * sin(VMS_4), \
        color = "blue", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 4$")
scatter(6 * cos(VMS_5), 6 * sin(VMS_5), \
        color = "purple", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 8$")
scatter(7 * cos(VMS_6), 7 * sin(VMS_6), \
        color = "orange", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 16$")
scatter(8 * cos(VMS_7), 8 * sin(VMS_7), \
        color = "black", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 32$")

legend()

axis("off")

title("Simulation Using Best & Fisher's Method for von Mises Distribution")

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 500)
