#!/bin/bash
echo -n Welcome to $HOSTNAME 
echo -n " "
getent passwd $USERNAME | cut -d ':' -f 5
echo You are currently logged in as $USERNAME, and your CWD is: 
pwd
echo -n The time is
date "+%l:%M%P"
