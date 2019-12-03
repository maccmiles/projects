#!/bin/bash

# Macchiarolim 11-17
# take stdin
# format input
# create group, user, passwd

#check args ((STDIN Only))
if [[ -t 0 ]]; then
  echo "usage: ./add_new_users.sh < file"
  exit 1
fi
######

#read line by line
while read LINE; do
    # goal 'adding NAME: USER, PASS'
    workingstr=$(echo "$LINE")
    firstName=$(echo "$workingstr" | cut -d ',' -f 1)
    lastName=$(echo "$workingstr" | cut -d ',' -f 2)
    initial=$(echo $lastName | head -c 1)
    useableUser=$(echo $firstName$initial | tr 'A-Z' 'a-z')
### Well here goes nothing
    checkUser=$useableUser
    count=1
    while getent passwd $checkUser  > /dev/null; do
        checkUser=$useableUser$count
#flippy floppies
        ((count++))
    done
    useableUser=$checkUser
    #heh suckers
### 
# Passgen
    cat /dev/urandom | tr -dc 'A-Za-z0-9' | head -c 8 > /tmp/pw.tmp
#    echo $workingstr
#    echo $firstName
#    echo $lastName
#    echo $firstName$initial
    echo adding $firstName $lastName: $useableUser, $(cat /tmp/pw.tmp)
# hope for the best
    groupadd $useableUser
    useradd -c "$firstName $lastName" -g $useableUser $useableUser
# set pass
    cat /tmp/pw.tmp | /usr/bin/passwd --stdin $useableUser > /dev/null
# wipe pass
    rm /tmp/pw.tmp
done < /dev/stdin
echo Finished.
