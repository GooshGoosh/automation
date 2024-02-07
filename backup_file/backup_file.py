'''
backup_file.py - This program takes a single command line argument as the path to
a file that the user would like to back up. The program will search for the file
and ensure that the file exists. Once the program has determined that the file exists,
it will then copy the file and save it as 'filename.ext.bak' in the same directory
as the original file.

Example: backupFile.py /home/user/example.txt <-- This will copy the example.txt file
and save the copy as example.txt.bak in /home/user/
'''

import sys
import os
import shutil


def main():
    """Main function to run the program.
    """
    # Ensure that a single command line argument is passed.
    if len(sys.argv) != 2:
        print('\nUsage: backup_file.py /path/to/file')
        sys.exit(1)

    path_to_file = sys.argv[1]

    # Ensure that the given argument is a file, not a directory, and that it exists.
    if os.path.isfile(os.path.abspath(path_to_file)):
        print('\nBacking up file...')
        new_file = path_to_file + '.bak'
        shutil.copy(path_to_file,new_file,follow_symlinks=False)
        print(f'\nFile saved as {new_file}')

if __name__ == "__main__":
    main()
