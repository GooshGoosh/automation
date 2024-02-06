'''
disk_usage.py - Checks the amount of space available on a disk and returns a
message depending on the space available.
'''

import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percent):
    """Checks the amount of space available on the given disk.
    Args:
        disk (str): Path to the disk to check.
        min_absolute (int): Minimum amount of space in GB to pass the test.
        min_percent (int): Minimum percentage of space to pass the test.
    Returns:
        bool: Whether the disk fails the test (False) or passes the test (True).
    """
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False

    return True


def main():
    """Main function to run the program.
    """
    if not check_disk_usage("/", 10, 15):
        print("ERROR: Not enough disk space.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)


if __name__ == "__main__":
    main()
