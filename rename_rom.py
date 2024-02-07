'''
rename_rom.py - Searches through a given directory, changes file names to have
a hyphen (-) between each word, and moves the renamed files to a given directory.
Mainly used to target and rename game ROM files.
'''


import re
import os
import subprocess
import sys


def main():
    """Main function to run the program.
    """
    if len(sys.argv) != 3:
        print('Usage: rename_rom.py [target directory] [destination directory]')
        sys.exit(0)

    target_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    special_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                         '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
                         '{', '|', '}', '~', '.']

    for file in os.listdir(target_dir):
        if os.path.isdir(file):
            continue

        old_file_path = os.path.join(target_dir, file)
        file_ext = os.path.splitext(file)[1]
        result = re.search(r"(.*)\(.*\)", file)
        if result is None:
            result = re.search(r"(.*)\.iso", file)
            if result is None:
                continue
        new_filename = result.group(1).lower().strip() + file_ext.lower()
        for char in special_chars:
            if char in new_filename:
                if char == "'":
                    new_filename = new_filename.replace(char, '')
                new_filename = new_filename.replace(char, ' ')
        new_filename = new_filename.replace('  ', ' ')
        new_filename = new_filename.replace(' ', '-')
        new_filename = new_filename.replace('--', '-')
        new_file_path = os.path.join(destination_dir, new_filename)
        subprocess.run(['cp', old_file_path, new_file_path], check=False)


if __name__ == "__main__":
    main()
