# argument 1 : the filename of input data
# argument 2 : the xlabel
# argument 3 : the ylabel

import os
import sys
from pylab import *

filenameRaw = sys.argv[1]
filenameCorrected = sys.argv[2]

lines = open(filenameRaw, "r").readlines();
XRaw = [line.strip().split()[0] for line in lines]
YRaw = [line.strip().split()[1] for line in lines]
XRaw = [float(x) for x in XRaw]
YRaw = [float(y) for y in YRaw]

lines = open(filenameCorrected, "r").readlines();
XCorrected = [line.strip().split()[0] for line in lines]
YCorrected = [line.strip().split()[1] for line in lines]
XCorrected = [float(x) for x in XCorrected]
YCorrected = [float(y) for y in YCorrected]

figure(figsize = (10, 5), dpi = 500)

scatter(XRaw, YRaw, c = "red", s = 10, alpha = 0.5, linewidths = 1,
        marker = u"+")
scatter(XCorrected, YCorrected, c = "blue", s = 10, alpha = 0.5, linewidths = 1,
        marker = u"+")

xlim(0, XRaw[-1])
ylim(0, 1)

xlabel(sys.argv[4])
ylabel(sys.argv[5])

savefig(sys.argv[3], dpi = 500)
