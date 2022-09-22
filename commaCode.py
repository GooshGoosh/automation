#!/usr/bin/env python3

# commaCode.py - Contains a function that takes a list value as an argument and returns a string with all the items seperated by 
# a comma and a space, with AND inserted before the last item.
# Works with any list value and prints 'Empty list' when an empty list value is passed to it.


spam = ['apples', 'bananas', 'tofu', 'cats']
emptyList = []
longList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']


def comma_join(itemList):
    newList = []
    if not itemList:
        print('Given list is empty')
    else:
        for i in range(len(itemList)):
            if itemList[i] == itemList[-1]:
                newList.append(f'and {itemList[i]}')
            else:
                newList.append(f'{itemList[i]}, ')
        print(''.join(newList))



def main():
    print()
    comma_join(spam)
    print()
    comma_join(emptyList)
    print()
    comma_join(longList)
    print()


if __name__ == "__main__":
    main()
