split -l 100000 train.csv part

for f in part*; do mv "$f" "$f.csv"; done

for f in part*;
do
    sort -t"," -n -k1 "$f" > "sorted_$f";
done

sort -m --parallel=8 -t"," -k1 sorted* > final_sorted.csv

for f in '../../BMTC/filtered_data/'*;
do
    python3 make_grid.py "${f:25:-1}v"
    echo{"${f:25:-1}v"}
done

for f in '../../BMTC/filtered_data/'*;
do
    python3 encode_grid.py "${f:25:-1}v"
    echo{"${f:25:-1}v"}
done

for f in '/home/ananya/Documents/BMTC/hundred/sorted_buses/'*;
do
    sort -t"," -n -k9 "$f" > "/home/ananya/Documents/BMTC/hundred/final_sorted/${f:49:-1}v";
    echo "${f:49:-1}v"
done

sort -m --parallel=8 -t"," -n -k8 "../../BMTC/sorted_encoded_data/"* > "../../BMTC/sorted_encoded_data/final_sorted.csv";