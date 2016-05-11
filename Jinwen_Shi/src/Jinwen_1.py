# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel

from pylab import *

filename = "../Data/data_1.txt"

X = []
Y = []

lines = open(filename, "r").readlines()

X = [line.strip().split("\t")[2] for line in lines[2:]]
Y = [line.strip().split("\t")[6] for line in lines[2:]]
name = [line.strip().split("\t")[0] for line in lines[2:]]

X_1 = []
Y_1 = []
name_1 = []

# List of Targeted Genes
nameList = ["Rn18s",
            "Zbtb20",
            "Aip",
            "Gnai2",
            "Gstt2",
            "Atf4",
            "Actb",
            "Ppp2r4",
            "Hip1r",
            "Blvrb",
            "Oxa1l",
            "Psmd11",
            "Smc4",
            "Srebf2",
            "Trpc4ap",
            "Hnrpdl",
            "Gng10",
            "Itpr3",
            "Sfpi1",
            "Itm2b",
            "Mrpl49",
            "Top1",
            "A430107D22Rik",
            "Letm1",
            "Mtdh",
            "Tbrg1",
            "Bcl6",
            "Clptm1l",
            "Gtf2i"]

# Remove NA of Y
for i in range(len(X)):
    if (Y[i] != "NA"):
        X_1.append(X[i])
        Y_1.append(Y[i])
        name_1.append(name[i])

# Wash the data
X_1 = [float(x) for x in X_1]
Y_1 = [-log(float(y)) / log(10) for y in Y_1]

# Indexing the target genes
geneIndex = [name_1.index(geneName) for geneName in nameList]
for index in range(len(Y_1)):
    if (Y_1[index] > 20):
        if name_1[index] not in geneIndex:
            geneIndex.append(index)

figure(figsize = (10, 10), dpi = 80)

cm = get_cmap("summer")
colors = [cm(y / 50) for y in Y_1]

scatter(X_1, Y_1, c = colors, s = 50, alpha = 1, linewidths = 0)

fontSize = 10

for index in geneIndex:
    annotate(name_1[index],
             xy = (X_1[index], Y_1[index]),
             xycoords = "data",
             xytext = (5, -5),
             textcoords = "offset points",
             fontsize = fontSize)

xlim(-2, 2)
ylim(0, 5)

xlabel(r"$\mathrm{log}_2\mathrm{FC}$")
ylabel(r"$-\mathrm{log}_{10} \mathrm{(p\ value)}$")

# Save the figure
savefig("../Figures/Jinwen_1.png", dpi = 200)
