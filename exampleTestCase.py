#!/user/bin/env python3

# exampleTestCase.py - Basic function to compare a given integer (n) with a list to find any items in the list that are greater than n.
# The function stores any numbers greater than n in a list and returns the list.

import unittest


# Function to run unit tests on.
def greater_than_num(num, listOfInt):
    greaterThanList = []
    if len(listOfInt) <= 0:
        return "Cannot compare against an empty list!"
    for item in listOfInt:
        if type(item) != int:
            raise TypeError("Items in list must be of type int!")
        if item > num:
            greaterThanList.append(item)
    return greaterThanList


# Create the function test class with the unittest.TestCase subclass.
class GreaterThanTest(unittest.TestCase):
    # Create the test functions; must start with "test" as the first word in the name.
    def test_base(self):
        testcase = greater_than_num(5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = [6, 7, 8, 9]
        self.assertEqual(testcase, expected)
        
    def test_empty_list(self):
        testcase = greater_than_num(5, [])
        expected = "Cannot compare against an empty list!"
        self.assertEqual(testcase, expected)

    def test_string_in_list(self):
        testcase = (5, [1, 2, 3, '4', 5, 6])
        expected = TypeError("Items in list must be of type int!")
        self.assertRaises(TypeError, greater_than_num, testcase, expected)
        
    def test_float_in_list(self):
        testcase = (5, [1, 2.2, 3, 4, 5, 6])
        expected = TypeError("Items in list must be of type int!")
        self.assertRaises(TypeError, greater_than_num, testcase, expected)
    
    def test_less_than_num(self):
        testcase = greater_than_num(5, [1, 2, 3, 4, 5])
        expected = []
        self.assertEqual(testcase, expected)
        
# Call the unittest class to run the tests.
unittest.main()