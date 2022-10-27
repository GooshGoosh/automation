#!/usr/bin/env python3

from hashlib import new
import re
import os
import subprocess
import sys


def main():
    if len(sys.argv) != 3:
        print('Usage: renameROM.py [target directory] [destination directory]')
        sys.exit(0)
        
    targetDirectory = sys.argv[1]
    destinationDirectory = sys.argv[2]
    specialCharacters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                         '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
                         '{', '|', '}', '~', '.']

    for file in os.listdir(targetDirectory):
        if os.path.isdir(file):
            continue
        else:
            oldFilePath = os.path.join(targetDirectory, file)
            fileExtension = os.path.splitext(file)[1]
            result = re.search(r"(.*)\(.*\)", file)
            if result is None:
                result = re.search(r"(.*)\.iso", file)
                if result is None:
                    continue
            newFilename = result.group(1).lower().strip() + fileExtension.lower()
            
            for char in specialCharacters:
                if char in newFilename:
                    if char == "'":
                        newFilename = newFilename.replace(char, '')
                    newFilename = newFilename.replace(char, ' ')
            newFilename = newFilename.replace('  ', ' ')
            newFilename = newFilename.replace(' ', '-')
            newFilename = newFilename.replace('--', '-')
            newFilePath = os.path.join(destinationDirectory, newFilename)
            
            subprocess.run(['cp', oldFilePath, newFilePath])


if __name__ == "__main__":
    main()
    
