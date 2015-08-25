from pylab import *
import matplotlib.patches as mpatches

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_Base.txt", "r").readlines();
XBase = [line.strip().split()[0] for line in lines]
YBase = [line.strip().split()[1] for line in lines]
XBase = [float(x) for x in XBase]
YBase = [float(y) for y in YBase]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_3.txt", "r").readlines();
X3_5 = [line.strip().split()[0] for line in lines]
Y3_5 = [line.strip().split()[1] for line in lines]
X3_5 = [float(x) for x in X3_5]
Y3_5 = [float(y) for y in Y3_5]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_6.txt", "r").readlines();
X6_8 = [line.strip().split()[0] for line in lines]
Y6_8 = [line.strip().split()[1] for line in lines]
X6_8 = [float(x) for x in X6_8]
Y6_8 = [float(y) for y in Y6_8]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_9.txt", "r").readlines();
X9_11 = [line.strip().split()[0] for line in lines]
Y9_11 = [line.strip().split()[1] for line in lines]
X9_11 = [float(x) for x in X9_11]
Y9_11 = [float(y) for y in Y9_11]

figure(figsize = (10, 5), dpi = 500)

colorBase = "black"
color3_5 = "blue"
color6_8 = "green"
color9_11 = "orange"

lw = 0.6
scatter(XBase, YBase, c = colorBase, linewidths = lw, marker = u"+")
scatter(X3_5, Y3_5, c = color3_5, linewidths = lw, marker = u"+")
scatter(X6_8, Y6_8, c = color6_8, linewidths = lw, marker = u"+")
scatter(X9_11, Y9_11, c = color9_11, linewidths = lw, marker = u"+")

xlim(0, 1000)
ylim(0, 1)

xlabel("Frequency")
ylabel("FRC")

patchBase = mpatches.Patch(color = colorBase, label = "Base")
patch3_5 = mpatches.Patch(color = color3_5, label = "3:5")

legend(handles = [patchBase, patch3_5])

title("FRC of a Corrected Stack")

savefig("../Figures/FRC_stack_1308.png", dpi = 500)
