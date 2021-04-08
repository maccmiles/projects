#!/bin/bash
newUser=$1
if getent passwd $newUser  > /dev/null; then
  echo "ERR: User already exists."
  exit 1
fi

echo "Provisioning user" $newUser
# Generate password
cat /dev/urandom | tr -dc 'A-Za-z0-9' | head -c 8 > /tmp/pw.tmp
echo adding $newUser, $(cat /tmp/pw.tmp)
useradd $newUser
#set pass
cat /tmp/pw.tmp | /usr/bin/passwd --stdin $newUser > /dev/null
#expire pass
passwd -e $newUser
echo "making sudo backup"
cp /etc/sudoers /etc/sudoers.bak
echo $newUser"      ALL=(ALL) ALL" | sudo tee -a /etc/sudoers > /dev/null
LOGMSG="Account Provision for $(hostname)"
echo New user $newUser created, login to $(hostname) with  $(cat /tmp/pw.tmp) | mailx -s "$LOGMSG" -S smtp=smtp://smtpout.esi.us.eisai.local $2

# wipe pass
    rm /tmp/pw.tmp

### 
