#!/usr/bin/env python3

# regexSearch.py - Takes a folder path and a user-supplied regular expression as command line arguments.
# The program then opens every .txt file and searches through the text to find a match for the provided regex.
# Any files that are found with a matching pattern are stored in a list and printed out for the user.


import re
import os
import sys


# Test that 3 arguments are given
if len(sys.argv) != 3:
    print('Usage: regexSearch.py [/path/to/folder] [regex]')
    sys.exit(0)

folderToSearch = sys.argv[1]
regexPattern = r"{}".format(sys.argv[2])
matchedFiles = []


def search_files(folder, pattern):
    # Search through the given path/folder for files that end with the txt extension,
    # open them, and search for the given pattern    
    for folder, subfolders, files in os.walk(os.path.abspath(folder)):
        if folder != os.path.abspath(folder):
            break
        else:
            for file in files:
                if file.lower().endswith('.txt'):
                    with open(os.path.join(folder, file), 'r') as data:
                        text = data.read()
                        result = re.search(pattern, text)
                        if result is not None:
                            matchedFiles.append(file)
                    data.close()
                else:
                    continue
                

# Output the list of files that contain a match of the given regex     
def output_list(list):
    print('\nFiles containing a matching pattern for ( {} ):'.format(regexPattern))
    for file in list:
        print(file)
    print()
                

def main():
    # Ensure that the given path/folder exists
    if not os.path.exists(folderToSearch):
        print('\nThe specified folder {} does not exist.\n'.format(folderToSearch))
        sys.exit(0)
    
    # Search through the files and print the output
    search_files(folderToSearch, regexPattern)
    output_list(matchedFiles)


if __name__ == "__main__":
    main()
