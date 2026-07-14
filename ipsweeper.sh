#!/usr/bin/env bash



read -p 'Enter Network Subnet: ' subnet


if [ "$subnet" == " " ]; then 
	echo "You forgot IP address"
	echo " Syntax: ./ipsweep 192.168.8"
else

for ip in `seq 1 254`; do
       	ping -c 1 $subnet.$ip  | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done 
fi




