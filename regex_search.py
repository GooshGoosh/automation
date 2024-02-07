'''
regex_search.py - Takes a directory path and a user-supplied regular expression as
command line arguments. The program then opens every .txt file and searches through
the text to find a match for the provided regex. Any files that are found with a
matching pattern are stored in a list and printed out for the user.
'''


import re
import os
import sys


# Test that 3 arguments are given
if len(sys.argv) != 3:
    print('Usage: regex_search.py [/path/to/folder] [regex]')
    sys.exit(0)

DIR_TO_SEARCH = sys.argv[1]
REGEX_PATTERN = f"{sys.argv[2]}"
matched_files = []


def search_files(folder, pattern):
    """Search through the given path/directory for files that end with the .txt
    extension, open them, and search for the given pattern.

    Args:
        folder (str): Directory to search through.
        pattern (str): Pattern to match in the .txt files.
    """
    for folder, subfolders, files in os.walk(os.path.abspath(folder)):
        if folder != os.path.abspath(folder):
            break

        for file in files:
            if file.lower().endswith('.txt'):
                with open(os.path.join(folder, file), 'r', encoding='UTF-8') as data:
                    text = data.read()
                    result = re.search(pattern, text)
                    if result is not None:
                        matched_files.append(file)
                data.close()
            else:
                continue

    
def output_list(file_list):
    """Output the list of files that contain a match of the given regex pattern.

    Args:
        list (_type_): _description_
    """
    print(f'\nFiles containing a matching pattern for ( {REGEX_PATTERN} ):')
    for file in file_list:
        print(file)
    print()


def main():
    """Main function to run the program.
    """
    # Ensure that the given path/folder exists
    if not os.path.exists(DIR_TO_SEARCH):
        print(f'\nThe specified folder {DIR_TO_SEARCH} does not exist.\n')
        sys.exit(0)

    # Search through the files and print the output
    search_files(DIR_TO_SEARCH, REGEX_PATTERN)
    output_list(matched_files)


if __name__ == "__main__":
    main()
