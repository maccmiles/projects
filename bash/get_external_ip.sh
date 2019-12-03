#!/bin/bash

#download index
wget -qO tmpip ipchicken.com
# search and save
grep -A 1 "Address" tmpip > ipc
#print ip
echo -n "Your External Address is: "
sed 's/[^0-9.]*//g' ipc

#remove file(s)
rm tmpip
rm ipc
