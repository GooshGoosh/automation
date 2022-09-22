#!/usr/bin/env python3

# binarySearch.py - Performs a binary search on a given list to find a given key/value


def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.

    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        if list[middle] < key:
            print("Checking the right side")
            left = middle + 1
    return -1 


def main():
    list = []
    binary_search(list, "")


if __name__ == "__main__":
    main()
