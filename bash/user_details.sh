#/bin/Bash
# MacchiaroliM
# 12/10/19
# noargs
# Print Full Name, Homedir, Num of files(home and sub, do not count dirs), owned processes, top 7 by mem
# 

#Get User List
usrList="$(users)"
#Split to array
IFS=' ' read -r -a usrArray <<< "$usrList"

# Loop for Array Length
for usrName in "${usrArray[@]}"
do
    usrRecord="$(getent passwd $usrName)"
    usrFQDN="$(echo "$usrRecord" | cut -d ':' -f 5)"
    usrHome="$(echo "$usrRecord" | cut -d ':' -f 6)"
    usrFiles="$(find "$usrHome" -type f | wc -l)"
    usrProc="$(ps -U "$usrName" | wc -l)"
    echo "User: $usrFQDN ($usrName)"
    echo "Home Directory: $usrHome"
    echo "Number of Files: $usrFiles"
    echo "Current Running processes: $usrProc"
    echo "Top 7 Processes by Memory Usage:"
    #Print Usage
    ps -u $usrName ux --sort -rss | head -n 7
    # Add spaces in between entries (if applicable)
    echo ""
    echo ""
done
