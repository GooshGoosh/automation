#!/bin/bash

# check-system-up.sh - Runs the ping command with a 2 second wait between each process to check if a system is able
# to be accessed remotely. The script takes one command line argument (the IP address of the target).

target=$1

echo -e "\nTesting for target: $target"
until ping -q -c 2 -W 1 $target > /dev/null; do
    echo "System is down..."
    sleep 2
done

echo -e "\n$target is up!\n"
