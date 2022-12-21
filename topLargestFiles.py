#!/usr/bin/env python3

''' 
topLargestFiles.py - Searches the directory given for the largest files (max 10) in the given directory.
Takes a single argument of a full path to a directory and finds the size of each file in the given directory.
The program then takes the 10 largest files found and puts them in a dictionary to print to the screen.
The list is printed to the screen starting with the largest size (shown in MB) and continuing in descending order.
If the directory given is empty or does not exist, then a simple line is printed to inform the user.
If the directory given contains less than 10 files, then the size of each file will be printed.
Any directories that are contained within the given directory will be put into a list and printed to the screen.
'''

import os
import sys


def get_directory_contents(directory):
    fullDirPath = os.path.abspath(directory)        # Get the absolute path of the directory.
    directoryContents = os.listdir(fullDirPath)     # Get the contents of the directory and store them in a list.
    return directoryContents


def get_size_of_contents(listOfContents, directory):
    directoryContentsSizes = {}
    listOfDirectories = []
    for item in listOfContents:
        if os.path.isdir(os.path.abspath(os.path.join(directory, item))):                         # Check if the item is a directory.
            listOfDirectories.append(item)                                                        # Add the item to the directory list.
        elif os.path.isfile(os.path.abspath(os.path.join(directory, item))):                      # Check if the item is a file.
            itemSize = os.path.getsize(os.path.abspath(os.path.join(directory, item)))            # Get the size of each file in the list.
            directoryContentsSizes[str(item)] = itemSize                                          # Store the file and its size in a dictionary for each file in the list.
    
    return sorted(directoryContentsSizes.items(), key=lambda item: item[1], reverse=True), listOfDirectories        # Return a sorted dictionary as a list of tuples containing the file name and size.


def print_largest_sizes(dictOfSizes):
    longestFilename = 0
    for i in range(len(dictOfSizes)):
        if len(dictOfSizes[i][0]) > longestFilename:        # Find the longest filename in the list
            longestFilename = len(dictOfSizes[i][0])        # to properly format the output.
    for i in range(len(dictOfSizes)):
        print('File: {} Size: {:.2f} MB'.format(str(dictOfSizes[i][0]).ljust((longestFilename + 3), "."), (dictOfSizes[i][1] / 1024**2)))       # Print the formatted output of the filename and the size.


def main():
    if len(sys.argv) != 2:      # Ensure that only one argument is given for the program.
        print("Usage: topLargestFiles.py [full dir path]")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):       # Ensure that the path argument given exists.
        print("Error: the given path does not exist. Exiting...")
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):        # Ensure that the path argument given is a directory and not a file.
        print("Error: the given path is not a directory. Exiting...")
        sys.exit(1)

    print("\n")
    directoryContents = get_directory_contents(directory=sys.argv[1])
    contentsSizes, listOfDirectories = get_size_of_contents(directoryContents, directory=sys.argv[1])
    print_largest_sizes(contentsSizes)
    print('\nList of directories contained within {} > {}'.format(sys.argv[1], ", ".join(listOfDirectories)))       # Print the list of directories that are in the given path argument for the program.


if __name__ == "__main__":
    main()
