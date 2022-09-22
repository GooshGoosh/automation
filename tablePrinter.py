#!/usr/bin/env python3

# tablePrinter.py - Contains a function that takes a list of strings and displays it in a well-organized table with each column right-justified.
# Assume the inner lists contain the same number of strings.


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    # Store the width of the longest string (table[0] =  colWidths[0], table[1] = colWdiths[1])
    colWidths = [0] * len(table)
    width = 0
    # Find the longest string in each of the inner lists so the whole column can be wide enough to fit all the strings
    # Store the maximum width of each column as a list of integers
    for i in range(len(table)):
        for k in range(len(table[i])):
            if len(table[i][k]) > colWidths[i]:
                colWidths[i] = len(table[i][k])
    
    # Store the largest value in colWidths
    for i in range(len(colWidths)):
        if colWidths[i] > width:
            width = colWidths[i]
            
    # rjust() print the first value of each of the inner lists in table[] while passing the colWidths value to the correct inner list
    for i in range(len(table[0])):
        for k in range(len(table)):
                print(f'{table[k][i].rjust(colWidths[k] + 1)}', end='')
        print()


def main():
    print_table(tableData)


if __name__ == "__main__":
    main()
