#! /bin/bash

iter=(0001 0005 0010 0015)

for i in ${iter[*]}
do
    scp humingxu@166.111.131.172:~/THUEM-refactor/case/Particle${i}.par \
        ../Data/Particle_Round_1
done

python Particle.py
