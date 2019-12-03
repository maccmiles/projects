#!/bin/bash
# 1 = existing file
# 2 = new file
# 3 = current 
# 4 = new
if [ "$1" == "" ]||[ "$2" == "" ]||[ "$3" == "" ]||[ "$4" == "" ]; then
    echo "Please include correct arguments"
else
    #Check valid file
    if [ ! -f $1 ];
    then
        echo "File does not exist"
    else
        #sed code || sed 's/foo/bar/g' hello.txtls
        sed -e 's/'$3'/'$4'/' $1 > $2
     fi

fi
