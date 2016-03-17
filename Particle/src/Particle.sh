for filename in `ls ../Data/*.txt`
do
    echo $filename
    python ParticleTest.py ../Data/$filename
done
