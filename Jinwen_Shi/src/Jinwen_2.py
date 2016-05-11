# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel

from pylab import *

filename = "../Data/data_2.txt"

X = []
Y = []

lines = open(filename, "r").readlines()

X = [line.strip().split("\t")[2] for line in lines]
Y = [line.strip().split("\t")[6] for line in lines]
name = [line.strip().split("\t")[0] for line in lines]

X_1 = []
Y_1 = []
name_1 = []

# List of Targeted Genes
nameListList = [["Bcl2", "Bmf", "Ccnb2", "Timeless"],
                ["Ccr6", "Ccr7", "S1pr1", "S1pr2", "S1pr4"],
                ["Cd38", "Cd55", "Cd97", "Il9r", "Ly6a", "Ly6d", "Sell"],
                ["Gpr183", "Nlrx1", "Mx1", "Tlr1", "Tlr7"],
                ["Bach2", "Bcl6", "Klf2", "Klf3", "Runx3", "Stat1", "Zbtb32"]]
# nameList = ["Cd38", "Ly6d", "S1pr1", "Klf2", "Ccr7", "Klf3", "Sell", "Il9r",
#             "Zbtb32", "Zfp238", "Ccr6", "Bcl6"]
nameList = []
for ls in nameListList:
    nameList += ls

# Remove NA of Y
for i in range(len(X)):
    if (Y[i] != "NA"):
        X_1.append(X[i])
        Y_1.append(Y[i])
        name_1.append(name[i])

# Remove the title
X_1.pop(0);
Y_1.pop(0);
name_1.pop(0);

# Wash the data
X_1 = [float(x) for x in X_1]
Y_1 = [-log(float(y)) / log(10) for y in Y_1]

# Indexing the target genes
geneIndex = [name_1.index(geneName) for geneName in nameList]
for index in range(len(Y_1)):
    if (Y_1[index] > 20):
        if name_1[index] not in geneIndex:
            geneIndex.append(index)

figure(figsize = (30, 30), dpi = 80)

# cm = get_cmap("summer")
# colors = [cm(y / 50) for y in Y_1]

scatter(X_1,
        Y_1, 
        c = "blue",
        s = [30 * y for y in Y_1],
        alpha = 0.7,
        linewidths = 0.7)

fontSize = 20

for index in geneIndex:
    annotate(name_1[index],
             xy = (X_1[index], Y_1[index]),
             xycoords = "data",
             xytext = (-100, 0),
             textcoords = "offset points",
             bbox = dict(boxstyle = "round", fc = "0.8"),
             arrowprops = dict(arrowstyle="->", linewidth = 2),
             fontsize = fontSize)

xlim(-6, 6)
ylim(0, 50)

xticks([-6, -4, -2, 0, 2, 4, 6], fontsize = 30)
yticks([0, 10, 20, 30, 40, 50], fontsize = 30)

xlabel(r"$\mathrm{log}_2\mathrm{FC}$", fontsize = 50)
ylabel(r"$-\mathrm{log}_{10} \mathrm{(p\ value)}$", fontsize = 50)

# change the border line size
[i.set_linewidth(2) for i in gca().spines.itervalues()]

# Save the figure
savefig("../Figures/Jinwe_2.png", dpi = 300)
