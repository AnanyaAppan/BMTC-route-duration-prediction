split -l 100000 train.csv part

for f in part*; do mv "$f" "$f.csv"; done

for f in part*;
do
    sort -t"," -k1 "$f" > "sorted_$f";
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

for f in '../../BMTC/encoded_data/'*;
do
    sort -t"," -n -k8 "$f" > "../../BMTC/sorted_encoded_data/${f:24:-1}v";
    echo "${f:24:-1}v"
done

sort -m --parallel=8 -t"," -n -k8 "../../BMTC/sorted_encoded_data/"* > "../../BMTC/sorted_encoded_data/final_sorted.csv";