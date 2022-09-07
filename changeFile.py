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
        newName.append(line.replace("jane", "jdoe"))
    for line in range(len(newName)):
        subprocess.run(['mv', oldName[line], newName[line]])
    file.close()

