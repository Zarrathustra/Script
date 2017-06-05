import Image # port py27-pil needed
import sys
import os

image = Image.open(sys.argv[1])
print "Before converting, the format is:"
print "Format = ", image.format
print "Size = ", image.size
print "Mode = ", image.mode

outFileName = os.path.splitext(sys.argv[1])[0] + ".png"

image.save(outFileName)
