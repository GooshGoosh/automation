#!/usr/bin/env python3

''' modifyImages.py - Takes a specified directory given as a single command line argument and searches through the directory
to determine any files that are images (e.g. files that can be opened with the pillow module's Image class). The files are then
displayed on the screen for the user to see and the user is asked if they would like to rotate, resize, or rename a file.
If the user chooses to modify a file, they are asked to select a file to perform the rotation, resize, or rename operation on.
Once the operation is complete, the user is asked if they would like to modify another file or exit the program. The process repeats
until the user decides to exit the program. '''


import os
import sys
from venv import create
from PIL import Image
import pyinputplus as pyip


# Ensure there is a single directory given as a command line argument.
if len(sys.argv) != 2:
    print('Usage: modifyImages.py [/path/to/directory]')
    sys.exit(1)

imageDirectory = os.path.abspath(sys.argv[1])

# Ensure the given directory path is valid.
if not os.path.isdir(imageDirectory):
    print('{} is not a valid directory!'.format(imageDirectory))

# Get the image files in the specified directory and place them into a list
def create_image_file_list(directory):
    images = []
    for file in os.listdir(directory):
        try:
            im = Image.open(os.path.join(directory, file))
            images.append(file)
            im.close()
        except IOError:
            continue
    return images


def main():
    imageFileList = create_image_file_list(imageDirectory)
    for file in imageFileList:
        print(file)


if __name__ == "__main__":
    main()
