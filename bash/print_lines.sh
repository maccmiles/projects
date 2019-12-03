#!/bin/bash
if [ "$1" == "" ]||[ "$2" == "" ]||[ "$3" == "" ]; then
    echo "Please include correct arguments"
else
    #Check valid file
    if [ ! -f $3 ];
    then
        echo "File does not exist"
    else
        #check starting length
        if [ $1 -le $(cat $3 | wc -l) ];
        then
            #check end length
            if [ $2 -lt $(cat $3 | wc -l) ];
            then
                head -n $1 $3 | tail -n $2
            else 
                echo "Invalid Ending Operator"
            fi
        else
            echo "Invalid Starting Operator"
        fi
     fi

fi
