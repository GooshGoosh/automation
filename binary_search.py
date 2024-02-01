'''
binary_search.py - Performs a binary search on a given list to find a given key/value.
'''


def binary_search(search_list, key):
    """Performs a binary search on the given list to find the given key.

    Args:
        search_list (list): List to search through.
        key (str): Key/value to search for.

    Returns:
        int: The position of the key in the list if found, -1 otherwise.
    """
    #List must be sorted:
    search_list.sort()
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if search_list[middle] == key:
            return middle
        if search_list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        if search_list[middle] < key:
            print("Checking the right side")
            left = middle + 1
    return -1


def main():
    """Main function to run the program.
    """
    search_list = []
    binary_search(search_list, "")


if __name__ == "__main__":
    main()
