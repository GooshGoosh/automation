''' 
top_largest_files.py - Searches the directory given for the largest files (max 10)
in the given directory. Takes a single argument of a full path to a directory and
finds the size of each file in the given directory. The program then takes the 10
largest files found and puts them in a dictionary to print to the screen. The list
is printed to the screen starting with the largest size (shown in MB) and continuing
in descending order. If the directory given is empty or does not exist, then a simple
line is printed to inform the user. If the directory given contains less than 10 files,
then the size of each file will be printed. Any directories that are contained within
the given directory will be put into a list and printed to the screen.
'''

import os
import sys


def get_directory_contents(directory):
    """Get the contents (files) of the given directory.

    Args:
        directory (str): Path/name to the directory to search.

    Returns:
        list: List of contents (files) in the given directory.
    """
    full_dir_path = os.path.abspath(directory)
    dir_contents = os.listdir(full_dir_path)
    return dir_contents


def get_size_of_contents(content_list, directory):
    """Get the size of the contents in the list given.

    Args:
        content_list (list): List of contents (files) from a given directory.
        directory (str): Path/name of the directory to search.

    Returns:
        _type_: _description_
    """
    dir_contents_sizes = {}
    list_of_dirs = []
    for item in content_list:
        if os.path.isdir(os.path.abspath(os.path.join(directory, item))):
            list_of_dirs.append(item)
        elif os.path.isfile(os.path.abspath(os.path.join(directory, item))):
            item_size = os.path.getsize(os.path.abspath(os.path.join(directory, item)))
            dir_contents_sizes[str(item)] = item_size

    return sorted(dir_contents_sizes.items(), key=lambda item: item[1],
                  reverse=True), list_of_dirs


def print_largest_sizes(list_of_sizes):
    """Print the 10 largest file sizes to the screen in MB.

    Args:
        list_of_sizes (list): List of tuples that contain the file names and the
        size of the file.
    """
    # Get the longest filename for formatting the output.
    longest_filename = 0
    for data in list_of_sizes:
        if len(data[0]) > longest_filename:
            longest_filename = len(data[0])

    for data in list_of_sizes:
        # Print the formatted output of the filename and the size in MB.
        print(f'File: {data[0].ljust((longest_filename + 3), ".")} \
            Size: {(data[1] / 1024**2):.2f} MB')


def main():
    """Main function to run the program.
    """
    # Ensure that only one argument is given for the program.
    if len(sys.argv) != 2:
        print("Usage: top_largest_files.py [full/dir/path]")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Error: the given path does not exist. Exiting...")
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print("Error: the given path is not a directory. Exiting...")
        sys.exit(1)

    print("\n")
    dir_contents = get_directory_contents(directory=sys.argv[1])
    if len(dir_contents) == 0:
        print("Given directory has no contents to parse. Exiting...")
        sys.exit(0)

    contents_sizes, list_of_dirs = get_size_of_contents(dir_contents, directory=sys.argv[1])
    print_largest_sizes(contents_sizes)
    print(f'\nList of directories contained within {sys.argv[1]} > \
        {", ".join(list_of_dirs)}')


if __name__ == "__main__":
    main()
