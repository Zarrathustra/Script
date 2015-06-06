#! /opt/local/bin/bash

monoPlot="Mono_Plot.py"
dualPlot="Dual_Plot.py"
barPlot="Bar.py"

monoPlotData=(
"Basic_General_Revenue.csv"
"Extend_General_Revenue.csv"
"Lost_Demand.csv"
)

dualPlotData=(
"Comparision_Demand00.csv"
"Comparision_Demand01.csv"
)

for filename in ${monoPlotData[*]}
do
    python ${monoPlot} ${filename}
done

for filename in ${dualPlotData[*]}
do
    python ${dualPlot} ${filename}
done

for filename in `ls bar`
do
    python ${barPlot} ${filename}
done
