# This script is for resizing an image
# argument 1 : input image filename
# argumnet 2 : width
# argument 3 : height

import Image # port py27-pil needed
import sys
import os

image = Image.open(sys.argv[1])
print "Before converting, the format is:"
print "Format = ", image.format
print "Size = ", image.size
print "Mode = ", image.mode

width = int(sys.argv[2])
height = int(sys.argv[3])

image = image.convert("RGBA").resize((width, height))

print "After converting, the format is:"
print "Format = ", image.format
print "Size = ", image.size
print "Mode = ", image.mode

image.save(sys.argv[1])
