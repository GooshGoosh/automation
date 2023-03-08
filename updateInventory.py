#!/usr/bin/env python3

'''
This program takes updates the "inventory" that is stored in a csv file. The csv file contains the item name, the item UPC code,
the price of the item, the current stock of the item, as well as a true/false value if the item is on sale or not.

The program takes two csv files as arguments and updates the first (original) file with the values from the second (source) file.
For each item in the source file, the original file is checked for the item and, if found, the UPC code is then checked to ensure that
the item is the same. If no item is found in the original file, then the UPC of each item is checked instead to ensure that an item
is found even if the item name value is changed. For example, if the original file had "apples" as an item with the UPC code "123-456" but
the source file had "red apples" as an item with the UPC code "123-456", then the program would still find the specified item instead of
adding a new entry to the inventory table.

If an item is not matched via name value of UPC code value, then the program will ask the user if they would like to create a new entry in the
original file for the item or if they would like to skip the item (this prevents the program from adding entries without the user's knowledge).
Any items that are in the original file and not in the source file will be untouched. Items that are no longer sold should either be deleted from
the original file directly or should be filled with a "0" for the item's stock value.

Once the file is full parsed and the inventory is updated, the program will ask the user if they would like to export the original file as a
spreadsheet file. Note that this will create a secondary copy of the original file (one file saved as .csv and one file saved as .xlsx).
This allows for a more human-readable version of the inventory.
'''

import sys
import os
import csv
import datetime
import shutil


def backup_original_inventory(originalInventory):
    print('\nBacking up original inventory...')

    today = datetime.datetime.now()                                                                     # Get today's date. 
    formatTime = today.strftime("%m-%d-%y")                                                             # Format today's date into the MM/DD/YY format. 
    filename = os.path.splitext(os.path.basename(originalInventory))                                    # Get the filename of the file without the file extension. 
    newFilename = '{}-backup-{}.csv'.format(filename[0], formatTime)                                    # Create the new filename for the backup file. 
    shutil.copy(originalInventory, os.path.join(os.path.dirname(originalInventory), newFilename))       # Make a backup copy of the original store inventory.

    print('\nOriginal inventory saved as {}'.format(os.path.join(os.path.dirname(originalInventory), newFilename)))


#def load_original_inventory(originalInventory):
#    with open(os.path.abspath(originalInventory)) as csvfile:


def main():
    # Check for the correct number of arguments passed to the program.
    if len(sys.argv) != 3:
        print('\nPlease provide the full path to the original inventory file and the updated inventory file.')
        print('Usage: updateInventory.py [/path/to/inventory.csv] [/path/to/updated/inventory.csv]')
        sys.exit(0)
    
    originalInventoryPath = sys.argv[1]
    updatedInventoryPath = sys.argv[2]

    backup_original_inventory(originalInventoryPath)


if __name__ == "__main__":
    main()

