
split -l 100000 train.csv part

for f in part*; do mv "$f" "$f.csv"; done

sort --parallel=8 -t"," -n -k1 part*

for f in part*;
do
    sort -t"," -k1 "$f" > "sorted_$f";
done

sort -m --parallel=8 -t"," -k1 sorted* > final_sorted.csv