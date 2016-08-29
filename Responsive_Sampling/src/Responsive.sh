#! /bin/bash

for src in `ls ../Data/$1/*_Final.par`
do
    echo $src
    ./Responsive_Sampling.exe $src
done
