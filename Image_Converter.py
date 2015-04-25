# This script is for converting an image to a 8-bit black and white image
# argument 1, the filename of input image
# argument 2 and argument 3 are optional. If given, this script will resize the
# image.

import Image # port py27-pil needed
import sys
import os

image = Image.open(sys.argv[1])
print "Before converting, the format is:"
print "Format = ", image.format
print "Size = ", image.size
print "Mode = ", image.mode

outFileName = os.path.splitext(sys.argv[1])[0] + ".bmp"

# mode L stands for 8-bit pixel, black and white

if (len(sys.argv) == 4):
    width = sys.argv[2]
    height = sys.argv[3]
    outImage = image.convert("L").resize((width, height))
elif (len(sys.argv) == 2):
    outImage = image.convert("L")
else:
    print "Wrong numbers of arguments"

outImage.save(outFileName)
