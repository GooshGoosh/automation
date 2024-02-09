#!/bin/bash
#
# backup-files.sh - Runs the backupFile.py script on any file specified.
# This allows the backupFile.py script to remain small while still allowing for
# multiple files to be backed up. This also allows for the backupFile.py script
# to remain independent of the OS that it is running on.


BACKUPSCRIPT=backup_file.py

echo -e "\nChecking for backup script..."

if [[ ! -e $BACKUPSCRIPT ]]; then
  echo -e "\nBackup script not found! Exiting..."
  exit
elif [[ ! -f $BACKUPSCRIPT ]]; then
  echo -e "\nBackup script file location is either a directory or a device file! Exiting"
  exit 
elif [[ ! -x $BACKUPSCRIPT ]]; then
  echo -e "\nBackup script does not have execute permissions for current user! Exiting..."
  exit
else
  $BACKUPSCRIPT #/path/to/file 
fi 

