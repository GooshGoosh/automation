#!/usr/bin/env python3

import sys
import subprocess


with open(sys.argv[1], 'r') as file:
    fileLines = file.readlines()
    oldName = []
    newName = []
    for line in fileLines:
        oldName.append(line.strip())
    for line in oldName:
        newName.append(line.replace(sys.argv[2], sys.argv[3]))
    for line in range(len(newName)):
        if sys.argv[2] in oldName[line]:
            subprocess.run(['mv', oldName[line], newName[line]])
    file.close()

