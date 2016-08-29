#! /bin/bash

N=`ls $1/Data/Particle/*.par | wc -l`
echo Number of Particles: $N

M=20
echo Maximum Number of Processes: $M

for src in `ls $1/Data/Particle/*.par`
do
    m=$(pgrep 'python' | wc -l)
    [[ $m -gt $M ]] && (wait)
    echo $src
    # idx=`echo ${src} | awk -F '/' '{print $NF}' | awk -F '_' '{print $2}'`
    dst=$1/Figures/Particle/`echo ${src} | awk -F '/' '{print $NF}' | awk -F '.' '{print $1}'`.png
    # python Particle.py $src $1/Data/Sampling_Points.par $idx $dst &
    python Particle.py $src $dst $2&
done
wait
