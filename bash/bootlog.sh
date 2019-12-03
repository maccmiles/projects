#!/bin/bash

# Macchiarolim 11-17
# take arg boot|shutdown
# log time | Host | Boot||Shutdown >> boot.log

#check args
if [[ $# -ne 1 ]]; then
  echo "usage: ./bootlog.sh boot|shutdown"
  exit 1
fi
######
ts=$(date)
if [ $1 == "boot" ] ; then
    echo $ts $HOSTNAME booted! >> ./home/macchiarolim/lab5/boot.log
    exit 0
elif [ $1 == "shutdown" ] ; then
    echo $ts $HOSTNAME shutdown! >> ./home/macchiarolim/lab5/boot.log
    exit 0
else
  echo "usage: ./bootlog.sh boot|shutdown"
  exit 1
fi
