#!/bin/bash

> oldFiles.txt

files=$(cat /home/student-03-d9b9a846c7d6/data/list.txt | grep ' jane ' | cut -d ' ' -f 3)

for file in $files; do
  if [ -e /home/student-03-d9b9a846c7d6$file ]; then
    echo "/home/student-03-d9b9a846c7d6$file" >> oldFiles.txt
  fi
done

