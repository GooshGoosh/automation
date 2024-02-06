'''
example_test_case.py - Basic function to compare a given integer (n) with a list
to find any items in the list that are greater than n. The function stores any
numbers greater than n in a list and returns the list.
'''


import unittest


def greater_than_num(num, list_of_int):
    """Compares a given num with a list of given numbers to check which number
    in the list is greater than the given num.

    Args:
        num (int): Number to compare against the list.
        list_of_int (list): List of integers to compare against the given num.

    Raises:
        TypeError: Ensures that items in the list are of type int.

    Returns:
        list: List of numbers greater than the given num.
    """
    greater_than_list = []
    if len(list_of_int) <= 0:
        return "Cannot compare against an empty list!"
    for item in list_of_int:
        if not isinstance(item, int):
            raise TypeError("Items in list must be of type int!")
        if item > num:
            greater_than_list.append(item)
    return greater_than_list


# Create the function test class with the unittest.TestCase subclass.
class GreaterThanTest(unittest.TestCase):
    """Test class for the greater_than_num function.
    """
    # Create the test functions.
    def test_base(self):
        """Base test to ensure the function works with the correct inputs.
        """
        testcase = greater_than_num(5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = [6, 7, 8, 9]
        self.assertEqual(testcase, expected)

    def test_empty_list(self):
        """Ensures the function handles an empty list properly.
        """
        testcase = greater_than_num(5, [])
        expected = "Cannot compare against an empty list!"
        self.assertEqual(testcase, expected)

    def test_string_in_list(self):
        """Ensures the function handles a str value in the list.
        """
        testcase = (5, [1, 2, 3, '4', 5, 6])
        expected = TypeError("Items in list must be of type int!")
        self.assertRaises(TypeError, greater_than_num, testcase, expected)

    def test_float_in_list(self):
        """Ensures the function handles a float value in the list.
        """
        testcase = (5, [1, 2.2, 3, 4, 5, 6])
        expected = TypeError("Items in list must be of type int!")
        self.assertRaises(TypeError, greater_than_num, testcase, expected)

    def test_less_than_num(self):
        """Ensures the function works with every number in the list being less than
        or equal to the given num to compare against.
        """
        testcase = greater_than_num(5, [1, 2, 3, 4, 5])
        expected = []
        self.assertEqual(testcase, expected)


# Call the unittest class to run the tests.
unittest.main()
