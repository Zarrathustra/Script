# This script can paste four images together.
# The four images must have equals size.

import Image
import os
import sys

upLeft = Image.open(sys.argv[1])
upRight = Image.open(sys.argv[2])
downLeft= Image.open(sys.argv[3])
downRight= Image.open(sys.argv[4])

if (upLeft.size == upRight.size == downLeft.size == downRight.size):
    result = Image.new("L", (upLeft.size[0] * 2, upLeft.size[1] * 2))
    result.paste(upLeft, (0, 0))
    result.paste(upRight, (upLeft.size[0], 0))
    result.paste(downLeft, (0, upLeft.size[1]))
    result.paste(downRight, (upLeft.size[0], upLeft.size[1]))
    result.save("pasted.bmp")
else:
    print "The four images must have equal size"
