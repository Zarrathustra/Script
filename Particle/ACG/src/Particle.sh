for filename in `ls ../Data/*.par`
do
    echo $filename
    python Quaternion_Polar.py ../Data/$filename
done
