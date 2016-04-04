#! /bin/bash

scp humingxu@166.111.131.172:~/THUEM-refactor/case/Sigma_\*.txt \
    ../Data/Sigma

python Sigma.py
