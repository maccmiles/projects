#!/bin/bash
#Print all IDS GE 1000 and MATCH shell
#Print all IDS GE 1000
#Skip all others
awk -F: '{if($3 >= 1000){if($7 == "/bin/bash" && $3 -ge "1000"){print $1}else{starIds=$1"*";print starIds}}}' /etc/passwd
