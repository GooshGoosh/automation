#!/usr/bin/env python3

# updateAllowList.py - Updates an allow list that contains IP addresses. Takes two command-line
# arguments; a file that contains a list of allowed IP addresses with each address on a separate line,
# and a file that contains a list of IP addresses to remove from the allow list with each address on
# a separate line.


import sys


def update_list(allowList, removeList):
    # Open and read the allow list and store the lines in a variable.
    with open(allowList, "r") as file:
        ipAddresses = file.read()
        ipAddresses = ipAddresses.split()

    # Open and read the remove list and store the lines in a variable.
    with open(removeList, "r") as file:
        removeAddresses = file.read()
        removeAddresses = removeAddresses.split()

    # Loop through removeAddresses list and remove any addresses from the ipAddresses
    # list that are in both lists.
    for address in removeAddresses:
        if address in ipAddresses:
            ipAddresses.remove(address)

    # Open the original allow list file and overwrite it with the updated list of
    # allowed IP address.
    with open(allowList, "w") as file:
        # Rejoin the ipAddresses list as a string with a newline character at the end of each address.
        ipAddresses = "\n".join(ipAddresses)
        file.write(ipAddresses)

    print("Allow list updated!")


def main():
    importFile = sys.argv[1]
    removeFile = sys.argv[2]

    update_list(importFile, removeFile)


if __name__ == "__main__":
    main()

