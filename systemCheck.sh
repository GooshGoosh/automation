#!/bin/bash

echo -e "\nStarting script to run system health check, system resource check, and a program to check the top 10 largest files in a given directory."
echo -e "\nFirst up is the system health check which will run a simple check on system resources.\n"

HEALTHCHECK=/home/alexg/scripts/automation/healthChecks.py
RESOURCECHECK=/home/alexg/scripts/automation/checkSystemResources.py
FILECHECK=/home/alexg/scripts/automation/topLargestFiles.py
FAILEDCHECKS=0


if [[ -e $HEALTHCHECK && -f $HEALTHCHECK && -x $HEALTHCHECK ]]; then
  echo -e "\nProgram found. Running simple health check..."
  $HEALTHCHECK
  echo -e "\nSimple health check complete."
else
  echo -e "\nHealth check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

if [[ -e $RESOURCECHECK && -f $RESOURCECHECK && -x $RESOURCECHECK ]]; then
  echo -e "\nProgram found. Running system resource check..."
  $RESOURCECHECK
  echo -e "\nSystem resource check complete."
else
  echo -e "\nSystem resource check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

if [[ -e $FILECHECK && -f $FILECHECK && -x $FILECHECK ]]; then
  echo -e "\nProgram found. Running file check..."
  $FILECHECK /home/alexg/iso-files/
  echo -e "\nFile check complete."
else
  echo -e "\nFile check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

echo -e "\nSystem check script complete. There were $FAILEDCHECKS failed checks."

