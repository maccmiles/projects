#!/bin/bash
# macchiarolim 11/11/19 (late)

# TODO
# use file, chmod,ls
# take an argument 
#check type of file and if exec
# check perms with ls -l
# if file is marked exec but is missing bits ask for verification and change



#check args
if [[ $# -ne 1 ]]; then
  echo "usage: ./fix_exec.sh filename"
  exit 1
fi
######


if file $1 | grep "executable"; then
#if file exec
    perms=$(stat -c '%a' $1) # I'm not really that into substrings, so if it's alright, I'll use octal instead
    if [ $perms == "775" ]; then
         echo "The file" \"$1\" "Is already marked as an executable, and has the permissions of 0775. There is nothing to do."
    else
         echo "The file" \"$1\" "Is marked as an executable, but does not have the corresponding permissions, would you like to add them (y/n)?"
         read choice
         if [ $choice == "y" ]; then
             chmod 0775 $1
             echo "permissions updated"
         else
             echo "no changes made"
		 fi
    fi
else
# if file not exec
    echo "File" \"$1\" "is not marked executable, make it executable (y/n)?"
    read choice
    if [ $choice == "y" ]; then
        chmod 0775 $1
        echo "permissions updated"
    else
        echo "no changes made"
    fi
fi
