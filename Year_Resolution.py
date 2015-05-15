from pylab import *
import matplotlib.patches as mpatches

filename = "Year_Resolution.csv"

# Data Reading and Checking 
# Collecting and Cleaning Data
lines = open(filename, "r").readlines();
X = [line.strip().split(",")[0] for line in lines]
Y = [line.strip().split(",")[1] for line in lines]
X = X[-6:]
Y = Y[-6:]
X = [int(x) for x in X]
Y = [float(y) for y in Y]

figure(figsize = (10, 5), dpi = 80)

alpha = 0.7

scatter(X, Y, alpha = 0.7, s = 100)

xticks(X, X)
xlabel("year")
ylabel(r"highest resolution achieved ($\AA$)")

savefig("Year_Resolution.png", dpi = 200)

show()
