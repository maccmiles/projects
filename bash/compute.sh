#!/bin/bash
echo -n "Enter an Interger: "
read int1
echo -n "Enter another Interger: "
read int2
echo -n "Enter an Operation (add,mul,div,mod,exp): "
read op

if [ $op == "add" ];
then
    echo $(($int1 + $int2))

elif [ $op == "sub" ];
then
    echo $(($int1 - $int2))

elif [ $op == "mul" ];
then
    echo $(($int1 * $int2))

elif [ $op == "div" ];
then
    echo $(($int1 / $int2))

elif [ $op == "mod" ];
then
    echo $(($int1 % $int2))

elif [ $op == "exp" ];
then
    echo $(($int1 ** $int2))
else
    echo "Please Enter A valid Value"
fi
