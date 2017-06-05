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

size = int(sys.argv[2])
# height = int(sys.argv[3])

left = image.size[0] / 2 - size / 2
top = 0
right = image.size[0] / 2 + size / 2
bottom = size

print left, top, right, bottom

image.crop((left, top, right, bottom)).save("test.bmp")
