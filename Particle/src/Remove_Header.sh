for filename in `ls ../Data/*.txt`
do
    sed -i.back '1d' $filename
done
