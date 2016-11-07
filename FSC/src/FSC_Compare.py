from pylab import *

import sys
import os

figure(figsize = (9, 6), dpi = 300)

lines = open("../Data/Sorzano_New_Compare/Sorzano.txt", "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

def plotFSC(filename, label, alpha):

    lines = open(filename, "r").readlines();

    Z = [float(line.strip().split()[2]) for line in lines]

    plot(X, Z, linewidth = 2, alpha = alpha, label = label)

plotFSC("../Data/Sorzano_New_Compare/Sorzano.txt", "Sorzano's Version", 1)

plotFSC("../Data/Sorzano_New_Compare/New.txt", "Our Version", 1)

xticks([30, 60, 90, 120, 150, 180], \
       ["$%.2f\AA$" %y for y in [Y[30 * 1], \
                                 Y[60 * 1], \
                                 Y[90 * 1], \
                                 Y[120 * 1], \
                                 Y[150 * 1], \
                                 Y[180 * 1]]], \
       rotation = "30")

xlim([0, 190])

#title("FSC Comparison between Sorzano's and Our Version")

xlabel('Resolution')
ylabel('FSC')

legend(loc = "upper right", \
       fontsize = "large")

subplots_adjust(top = 0.9, bottom = 0.2)

savefig("../Figures/Sorzano_New_Compare.png", dpi = 300)
