from pylab import *

import sys
import os

figure(figsize = (10, 5), dpi = 300)

lines = open("../Data/CTF_Vari/CTF_20000.txt", "r").readlines();

X = [float(line.strip().split()[0]) for line in lines]
Y = [float(line.strip().split()[1]) for line in lines]

def plotFSC(filename, label, alpha):

    lines = open(filename, "r").readlines();

    Z = [float(line.strip().split()[2]) for line in lines]

    plot(X, Z, linewidth = 2, alpha = alpha, label = label)

plotFSC("../Data/CTF_Vari/CTF_19800.txt", "-2%", 0.5)

#plotFSC("../Data/CTF_Vari/CTF_20000.txt", "Defocus = 20000 Angstrom", 1) 
plotFSC("../Data/CTF_Vari/CTF_20000.txt", "$\Delta f = 20000\AA$", 1)

plotFSC("../Data/CTF_Vari/CTF_20200.txt", "+2%", 0.5)

xticks([120, 130, 140, 150, 160, 170, 180], \
       ["$%.2f\AA$" %y for y in [Y[120 * 100], \
                                 Y[130 * 100], \
                                 Y[140 * 100], \
                                 Y[150 * 100], \
                                 Y[160 * 100], \
                                 Y[170 * 100], \
                                 Y[180 * 100]]],
       rotation = "30")

xlim([120, 190])

xlabel('Resolution')
ylabel('CTF')

legend(loc = "upper right", \
       bbox_to_anchor = (1, 1.35),
       fontsize = "medium")

subplots_adjust(top = 0.75, bottom = 0.2)

savefig("../Figures/FSC_Compare.png", dpi = 300)
