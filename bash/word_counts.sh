#!/bin/bash
#read line by line
tmpnum=1
total=0
while read LINE; do
    echo -n Line $tmpnum: 
    echo -n " "
    tmptotal=$(echo "$LINE" | wc -w)
    echo $tmptotal
    tmpnum=$(($tmpnum+1))
    total=$(($total+$tmptotal))
done < /dev/stdin
echo Total: $total
