#! /bin/bash

for (( i = 15; i<=28; i+=3 ))
do
    python FRCFittingApp.py ../Data/FRC_stack_1308/FRC_stack_1308_2x_Corrected_$i.txt \
        3838 17963 18713 0.0196 1.32 0 1350 180 1300
done
