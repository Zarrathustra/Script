# the first two arguments are width and height
# the following arguments will be the images to be resized

width=$1
shift

height=$1
shift

while [ $# -ne 0 ]
do
    python Image_Resizer.py $1 ${width} ${height}
    shift
done
