#!/bin/bash

echo -e "\nStarting script to run system health check, system resource check, and a program to check the top 10 largest files in a given directory."
echo -e "\nFirst up is the system health check which will run a simple check on system resources.\n"

HEALTHCHECK=health_check/health_checks.py
RESOURCECHECK=check_system_resources.py
FILECHECK=top_largest_files.py
FAILEDCHECKS=0


if [[ -e $HEALTHCHECK && -f $HEALTHCHECK && -x $HEALTHCHECK ]]; then
  echo -e "\nProgram found. Running simple health check..."
  python3 $HEALTHCHECK
  echo -e "\nSimple health check complete."
else
  echo -e "\nHealth check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

if [[ -e $RESOURCECHECK && -f $RESOURCECHECK && -x $RESOURCECHECK ]]; then
  echo -e "\nProgram found. Running system resource check..."
  python3 $RESOURCECHECK
  echo -e "\nSystem resource check complete."
else
  echo -e "\nSystem resource check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

if [[ -e $FILECHECK && -f $FILECHECK && -x $FILECHECK ]]; then
  echo -e "\nProgram found. Running file check..."
  python3 $FILECHECK .
  echo -e "\nFile check complete."
else
  echo -e "\nFile check program not found!"
  FAILEDCHECKS=$((++FAILEDCHECKS))
fi

echo -e "\nSystem check script complete. There were $FAILEDCHECKS failed checks."

