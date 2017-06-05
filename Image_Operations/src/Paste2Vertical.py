# This script can paste two images together vertically.
# The two images must have equals size.

import Image
import os
import sys

left = Image.open(sys.argv[1])
right = Image.open(sys.argv[2])

if (left.size != right.size):
    print "The two images do not have equal size."
else:
    result = Image.new("L", (left.size[0], left.size[1] * 2))
    result.paste(left, (0, 0))
    result.paste(right, (0, left.size[1]))
    result.save("pasted.bmp")
