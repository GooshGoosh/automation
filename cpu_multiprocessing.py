'''
cpu_multiprocessing.py - Simple program that shows an example of using multiprocessing
to speed up program operations.
'''

import multiprocessing
import time


def cpu_bound(number):
    """Takes a number and multiplies every number up to the value of the given
    number and multiplies it by itself then sums up all of those results.

    Args:
        number (int): An arbitrary number.

    Returns:
        int: The sum of values of each number multiplied by itself up to the
        value of the given number.
    """
    return sum(i * i for i in range(number))


def find_sums(numbers):
    """Takes a list of numbers and uses multiprocessing to get the sum of each
    number multiplied by itself up to the value of each number in the list.

    Args:
        numbers (list): list of arbitrary numbers.
    """
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)

if __name__ == "__main__":
    nums = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(nums)
    duration = time.time() - start_time
    print(f"Duration: {duration} seconds")
