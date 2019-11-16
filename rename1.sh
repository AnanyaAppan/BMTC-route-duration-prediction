for f in sorted_part*;
do
    python ../BMTC-route-duration-prediction/remove_zeros.py "$f";
done

sort -m --parallel=8 -t"," -k1 sorted* > final_sorted.csv