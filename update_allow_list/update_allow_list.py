'''
update_allow_list.py - Updates an allow list that contains IP addresses.
Takes two command line arguments; a file that contains a list of allowed IP addresses
with each address on a separate line, and a file that contains a list of IP addresses
to remove from the allow list with each address on a separate line.
'''


import sys


def update_list(allow_list, remove_list):
    """Upates the given allow list by removing the addresses in the given remove list.

    Args:
        allow_list (str): Path to the allowed list of IP addresses.
        remove_list (str): Path to the list of IP addresses to remove.
    """
    # Open and read the allow list and store the lines in a variable.
    with open(allow_list, "r", encoding='UTF-8') as file:
        ip_addresses = file.read()
        ip_addresses = ip_addresses.split()

    # Open and read the remove list and store the lines in a variable.
    with open(remove_list, "r", encoding='UTF-8') as file:
        remove_addresses = file.read()
        remove_addresses = remove_addresses.split()

    # Loop through remove_addresses list and remove any addresses from the ip_addresses
    # list that are in both lists.
    for address in remove_addresses:
        if address in ip_addresses:
            ip_addresses.remove(address)

    # Open the original allow list file and overwrite it with the updated list of
    # allowed IP address.
    with open(allow_list, "w", encoding='UTF-8') as file:
        # Rejoin the ip_addresses list as a string with a newline character
        # at the end of each address.
        ip_addresses = "\n".join(ip_addresses)
        file.write(ip_addresses)

    print("Allow list updated!")


def main():
    """Main function to run the program.
    """
    import_file = sys.argv[1]
    remove_file = sys.argv[2]

    update_list(import_file, remove_file)


if __name__ == "__main__":
    main()
