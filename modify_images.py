'''
modify_images.py - Takes a specified directory given as a single command line
argument and searches through the directory to determine any files that are images
(e.g. files that can be opened with the pillow module's Image class). The files are
then displayed on the screen for the user to see and the user is asked if they would
like to rotate or resize a file. If the user chooses to modify a file, they are
asked to select a file to perform the rotation or resize operation on. The file
is saved under a new name depending on the action taken.
Once the operation is complete, the user is asked if they would like to modify
another file or exit the program. The process repeats until the user decides to exit
the program. '''


import os
import sys
from pathlib import Path
from PIL import Image
import pyinputplus as pyip


# Ensure there is a single directory given as a command line argument.
if len(sys.argv) != 2:
    print('Usage: modify_images.py [/path/to/directory]')
    sys.exit(1)

IMAGE_DIR = os.path.abspath(sys.argv[1])

# Ensure the given directory path is valid.
if not os.path.isdir(IMAGE_DIR):
    print(f'{IMAGE_DIR} is not a valid directory!')

# Get the image files in the specified directory and place them into a list
def create_image_file_list(directory):
    """Creates a list of image files found in the given directory.

    Args:
        directory (str): Path to a directory on the system.

    Returns:
        list: List of images found in the given directory.
    """
    images = []
    for file in os.listdir(directory):
        try:
            im = Image.open(os.path.join(directory, file))
            images.append(file)
            im.close()
        except IOError:
            continue
    return images


def rotate_image(image_list, directory):
    """Rotates a selected image from the given list of image files.

    Args:
        image_list (list): List of image files.
        directory (str): Path to the directory containing the image files.
    """
    image_file = pyip.inputMenu(image_list, prompt='\nSelect an image to rotate:\n',
                                numbered=True)
    rotation = pyip.inputInt(prompt='\nEnter the degrees to rotate the image couter clockwise: ')

    image_name = Path(image_file).stem
    image_suffix = Path(image_file).suffix
    new_name = image_name + f'_rotated_{rotation}' + image_suffix

    im = Image.open(os.path.join(directory, image_file))
    im.rotate(rotation)
    im.save(os.path.join(directory, new_name))
    im.close()

    print(f'\nImage saved as {new_name} in {directory}')


def resize_image(image_list, directory):
    """Resizes a selected image from the given list of image files.

    Args:
        image_list (list): List of image files.
        directory (str): Path to the directory containing the image files.
    """
    image_file = pyip.inputMenu(image_list, prompt='\nSelect an image to resize:\n',
                                numbered=True)
    width = pyip.inputInt(prompt='\nEnter the new width of the image: ')
    height = pyip.inputInt(prompt='Enter the new height of the image: ')

    image_name = Path(image_file).stem
    image_suffix = Path(image_file).suffix
    new_name = image_name + f'_{width}x{height}' + image_suffix

    im = Image.open(os.path.join(directory, image_file))
    im.resize(size=(width, height))
    im.save(os.path.join(directory, new_name))
    im.close()

    print(f'\nImage saved as {new_name} in {directory}')


def main():
    """Main function to run the program.
    """
    image_file_list = create_image_file_list(IMAGE_DIR)

    if not image_file_list:
        print(f'\nThere are no images files in {IMAGE_DIR}')
        sys.exit(0)

    for file in image_file_list:
        print(file)

    while True:
        action = pyip.inputMenu(['Rotate', 'Resize', 'Exit'], prompt='\nChoose an action:\n',
                                numbered=True)
        if action == 'Rotate':
            rotate_image(image_file_list, IMAGE_DIR)
        elif action == 'Resize':
            resize_image(image_file_list, IMAGE_DIR)
        else:
            sys.exit(0)


if __name__ == "__main__":
    main()
