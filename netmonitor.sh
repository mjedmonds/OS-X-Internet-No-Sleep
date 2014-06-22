#!/bin/bash
#prints netstats bytes sum every 10 seconds

echo $(date)

read sum <<< $( /usr/local/bin/gtimeout 12s netstat -b -n 10 |awk '{sum += $3; if(sum != 0) print sum}' )

#allow sleep if the sum of the traffic is less than 60 KB
if [ $sum -lt 60000 ] 
then 
   sudo pmset -c sleep 20
   echo "pmset -c sleep 20"
#otherwise set no sleep
else
   sudo pmset -c sleep 0
   echo "pmset -c sleep 0"
fi

echo $sum
