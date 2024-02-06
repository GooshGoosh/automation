'''
find_images.py - Searches a given directory for image files.
'''


import sys
import os
from PIL import Image


if len(sys.argv) != 2:
    print("Usage: find_images.py [/path/to/directory]")

IMAGE_DIR = sys.argv[1]


def main():
    """Main function to run the program.
    """
    print()
    for file in os.listdir(IMAGE_DIR):
        try:
            im = Image.open(os.path.join(IMAGE_DIR, file))
        except IOError:
            continue

        print(f'{file} is an image file in {IMAGE_DIR}')
        im.close()
    print()

if __name__ == "__main__":
    main()
