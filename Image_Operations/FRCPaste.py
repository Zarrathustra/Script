import Image
import os
import sys

left = Image.open(sys.argv[1])
right = Image.open(sys.argv[2])

width = right.size[0]
left = left.resize((width, width))

result = Image.new("RGBA", (width, width + right.size[1]))
result.paste(left, (0, 0))
result.paste(right, (0, left.size[1]))
result.save("pasted.png")
