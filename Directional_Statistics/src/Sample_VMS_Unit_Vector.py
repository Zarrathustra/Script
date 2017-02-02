from pylab import *
import os

filename = sys.argv[1]

lines = open(filename, "r").readlines();

VMS_0_X = array([float(line.strip().split()[0]) for line in lines])
VMS_0_Y = array([float(line.strip().split()[1]) for line in lines])
VMS_1_X = array([float(line.strip().split()[2]) for line in lines])
VMS_1_Y = array([float(line.strip().split()[3]) for line in lines])
VMS_2_X = array([float(line.strip().split()[4]) for line in lines])
VMS_2_Y = array([float(line.strip().split()[5]) for line in lines])
VMS_3_X = array([float(line.strip().split()[6]) for line in lines])
VMS_3_Y = array([float(line.strip().split()[7]) for line in lines])
VMS_4_X = array([float(line.strip().split()[8]) for line in lines])
VMS_4_Y = array([float(line.strip().split()[9]) for line in lines])
VMS_5_X = array([float(line.strip().split()[10]) for line in lines])
VMS_5_Y = array([float(line.strip().split()[11]) for line in lines])
VMS_6_X = array([float(line.strip().split()[12]) for line in lines])
VMS_6_Y = array([float(line.strip().split()[13]) for line in lines])
VMS_7_X = array([float(line.strip().split()[14]) for line in lines])
VMS_7_Y = array([float(line.strip().split()[15]) for line in lines])

figure(figsize = (10, 10), dpi = 500)

scatter(VMS_0_X, VMS_0_Y, \
        color = "red", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 0$")
scatter(2 * VMS_1_X, 2 * VMS_1_Y, \
        color = "orange", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 0.5$")
scatter(3 * VMS_2_X, 3 * VMS_2_Y, \
        color = "yellow", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 1$")
scatter(4 * VMS_3_X, 4 * VMS_3_Y, \
        color = "green", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 2$")
scatter(5 * VMS_4_X, 5 * VMS_4_Y, \
        color = "blue", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 4$")
scatter(6 * VMS_5_X, 6 * VMS_5_Y, \
        color = "purple", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 8$")
scatter(7 * VMS_6_X, 7 * VMS_6_Y, \
        color = "brown", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 16$")
scatter(8 * VMS_7_X, 8 * VMS_7_Y, \
        color = "black", \
        linewidth = 0, alpha = 0.1, \
        label = "$\kappa = 32$")

xlim([-10, 10])
ylim([-10, 10])

legend()

axis("off")

title("Simulation Using Best & Fisher's Method for von Mises Distribution")

basename = os.path.basename(filename)
basename = os.path.splitext(basename)[0]

savefig("../Figures/" + basename + ".png", dpi = 500)
