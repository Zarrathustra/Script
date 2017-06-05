# This script can paste three images together.
# The three images must have equals size.

import Image
import os
import sys

left = Image.open(sys.argv[1])
middle = Image.open(sys.argv[2])
right = Image.open(sys.argv[3])

if (left.size == middle.size == right.size):
    result = Image.new("L", (left.size[0] * 3, left.size[1]))
    result.paste(left, (0, 0))
    result.paste(middle, (left.size[0], 0))
    result.paste(right, (left.size[0] * 2, 0))
    result.save("pasted.bmp")
else:
    print "Images must have equal size."
