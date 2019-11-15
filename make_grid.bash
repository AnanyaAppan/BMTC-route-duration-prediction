
# awk -F '","'  'BEGIN {OFS=","} { if $5 == "STRING 1")  print }' file1.csv > file2.csv

i=0
j=0
for lat in $(seq 12.66 0.008 13.32); do
    for long in $(seq 77.27  0.023 78); do
        echo $lat
        echo $long
        touch "../../BMTC/gridData/grid_${i}_${j}.csv"
        let j=j+1
    done
    let j=0
    let i=i+1
done

for f in '../../BMTC/filtered_data/'*;
do
    i=0
    j=0
    echo $f
    for lat in $(seq 12.66 0.008 13.32); do
        for long in $(seq 77.27  0.023 78); do
            GRID="../../BMTC/gridData/grid_${i}_${j}.csv"; > $GRID
            awk -F ","  'BEGIN {OFS=","} { if (($3 >= $lat) && ($3 < $lat+0.008) && ($4 >= $long) && ($4 < $long+0.023))  print }' $f >> $GRID
            let j=j+1
        done
        let j=0
        let i=i+1
    done
done

awk -F ","  'BEGIN {OFS=","} { if ($2=="32")  print }' "weatherdata.csv" >>"ran.csv"


awk -F ","  'BEGIN {OFS=","} { if ($2>=32 && $2<35)  print }' "weatherdata.csv"

for f in '../../BMTC/filtered_data/'*;
do
    i=0
    j=0
    echo $f
    lat = 
    GRID="../../BMTC/gridData/grid_${i}_${j}.csv"; > $GRID
    awk -F ","  'BEGIN {OFS=","} { if (($3 >= $lat) && ($3 < $lat+0.008) && ($4 >= $long) && ($4 < $long+0.023))  print }' $f >> $GRID
    let j=j+1
       
done