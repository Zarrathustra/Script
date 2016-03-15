from pylab import *

filename = "../Data/Group_MicID.txt"

lines = open(filename, "r").readlines();

X = [int(line.strip().split()[0]) for line in lines]
Y = [int(line.strip().split()[1]) for line in lines]

figure(figsize = (10, 10), dpi = 500)

print "Min of Group = ", min(X)
print "Max of Group = ", max(X)

print "Min of Micrograph = ", min(Y)
print "Max of Micrograph = ", max(Y)

scatter(X, Y, color = "black", alpha = 0.02, linewidth = 0)

xlim([0, 220])
ylim([0, 220])

xlabel("Index of Group")
ylabel("Index of Micrograph")

title("Correlation between GroupID and MicrographID")

savefig("../Figures/Group_MicID.png", dpi = 500)
