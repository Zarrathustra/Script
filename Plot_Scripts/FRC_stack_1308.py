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

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_12.txt", "r").readlines();
X12_14 = [line.strip().split()[0] for line in lines]
Y12_14 = [line.strip().split()[1] for line in lines]
X12_14 = [float(x) for x in X12_14]
Y12_14 = [float(y) for y in Y12_14]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_15.txt", "r").readlines();
X15_17 = [line.strip().split()[0] for line in lines]
Y15_17 = [line.strip().split()[1] for line in lines]
X15_17 = [float(x) for x in X15_17]
Y15_17 = [float(y) for y in Y15_17]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_18.txt", "r").readlines();
X18_20 = [line.strip().split()[0] for line in lines]
Y18_20 = [line.strip().split()[1] for line in lines]
X18_20 = [float(x) for x in X18_20]
Y18_20 = [float(y) for y in Y18_20]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_21.txt", "r").readlines();
X21_23 = [line.strip().split()[0] for line in lines]
Y21_23 = [line.strip().split()[1] for line in lines]
X21_23 = [float(x) for x in X21_23]
Y21_23 = [float(y) for y in Y21_23]

lines = open("../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_21.txt", "r").readlines();
X24_26 = [line.strip().split()[0] for line in lines]
Y24_26 = [line.strip().split()[1] for line in lines]
X24_26 = [float(x) for x in X24_26]
Y24_26 = [float(y) for y in Y24_26]
figure(figsize = (10, 5), dpi = 500)

colorBase = "black"
color3_5 = "blue"
color6_8 = "green"
color9_11 = "lightgreen"
color12_14 = "yellow"
color15_17 = "orange"
color18_20 = "red"
color21_23 = "purple"
color24_26 = "magenta"

lw = 0.3
scatter(XBase, YBase, c = colorBase, linewidths = lw, marker = u"+")
scatter(X3_5, Y3_5, c = color3_5, linewidths = lw, marker = u"+")
scatter(X6_8, Y6_8, c = color6_8, linewidths = lw, marker = u"+")
scatter(X9_11, Y9_11, c = color9_11, linewidths = lw, marker = u"+")
scatter(X12_14, Y12_14, c = color12_14, linewidths = lw, marker = u"+")
scatter(X15_17, Y15_17, c = color15_17, linewidths = lw, marker = u"+")
scatter(X18_20, Y18_20, c = color18_20, linewidths = lw, marker = u"+")
scatter(X21_23, Y21_23, c = color21_23, linewidths = lw, marker = u"+")
scatter(X24_26, Y24_26, c = color24_26, linewidths = lw, marker = u"+")

xlim(0, 1000)
ylim(0, 1)

xlabel("Frequency")
ylabel("FRC")

patchBase = mpatches.Patch(color = colorBase, label = "Base")
patch3_5 = mpatches.Patch(color = color3_5, label = "3:5")
patch6_8 = mpatches.Patch(color = color6_8, label = "6:8")
patch9_11 = mpatches.Patch(color = color9_11, label = "9:11")
patch12_14 = mpatches.Patch(color = color12_14, label = "12:14")
patch15_17 = mpatches.Patch(color = color15_17, label = "15:17")
patch18_20 = mpatches.Patch(color = color18_20, label = "18:20")
patch21_23 = mpatches.Patch(color = color21_23, label = "21:23")
patch24_26 = mpatches.Patch(color = color24_26, label = "24:26")

legend(handles = [patchBase,
                  patch3_5,
                  patch6_8,
                  patch9_11,
                  patch12_14,
                  patch15_17,
                  patch18_20,
                  patch21_23,
                  patch24_26])

title("FRC of a Corrected Stack")

savefig("../Figures/FRC_stack_1308.png", dpi = 500)
