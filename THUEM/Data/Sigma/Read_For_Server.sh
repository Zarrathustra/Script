#! /bin/bash

iter=(00 01)

for i in ${iter[*]}
do
    scp humingxu@166.111.131.172:~/THUEM-refactor/case/Sigma_${i}.txt .
done
