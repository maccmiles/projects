#!/bin/bash

# Macchiarolim 12-1
# get net info
# dyn/sta
# grep/awk

###

# dynamic ipv4 address: x.x.x.x
# MAC Address: *:*:*:*:*:*
# Gateway Router: x.x.x.x
# DNS Server: x.x.x.x
# DNS Server: x.x.x.x
# DNS domain: wit.private
# DNS domain: comp3100
# NIC speed: 100Mb/s
# NIC duplex: Full


#check sudo
if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Operation not permitted"
    exit
fi

# check args
if [[ $# -gt 1 ]]; then
    echo "usage: sudo ./get_network_info.sh <interface> (default: ens37)"
    exit
fi

# if no interface supplied
if [[ $# -ne 1 ]]; then
    adapter="ens37"
else
  adapter=$1
fi
##set vars
dhcpStatus=$(ip a | awk '/'$adapter'/ {print $8}' | tail -n 1)
ipWithSubnet=$(ip a | awk '/'$adapter'/ {print $2}' | tail -n 1)
adptrSpeed=$(/sbin/ethtool $adapter | awk '/Speed/ {print}' | sed -e 's/^[[:space:]]*//')
adptrDuplex=$(/sbin/ethtool $adapter | awk '/Duplex/ {print}' | sed -e 's/^[[:space:]]*//')
hwAddr=$(ip a s $adapter | awk '/link/ {print $2}' | head -n 1)
currentState=$(cat /sys/class/net/$adapter/operstate)
gatewayIP=$(ip route | awk '/default/ {print $3}')
dnsServers=$(nmcli dev show | awk '/DNS/ {print $2}')
dnsDomains=$(nmcli dev show | awk '/DOMAIN/ {print $2}')
echo "Current Adapter: $adapter"
echo "IPv4 Address: $ipWithSubnet"
echo "Type: $dhcpStatus"
echo "Adapter State: $currentState"
echo "MAC Address: $hwAddr"
echo "Gateway router: $gatewayIP"
####PRINT DNS
for item in $dnsServers; do
    echo "DNS Server: $item"
done
####PRINT Domain
for item in $dnsDomains; do
    echo "DNS Domain: $item"
done
echo "NIC $adptrSpeed"
echo "NIC $adptrDuplex"
