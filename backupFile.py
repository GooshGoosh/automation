#!/usr/bin/env python3

"""
backupFile.py - This program takes a single command-line argument as the path to a file that the user would like to back up.
The program will search for the file and ensure that the file exists. Once the program has determined that the file exists,
it will then copy the file and save it as 'filename.ext.bak' in the same directory as the original file.

Example: backupFile.py /home/user/example.txt <-- This will copy the example.txt file and save the copy as example.txt.bak in /home/user/
"""

import sys
import os
import shutil


def main():
    if len(sys.argv) != 2:
        print('\nUsage: backupFile.py /path/to/file')
        sys.exit(1)


if __name__ == "__main__":
    main()

