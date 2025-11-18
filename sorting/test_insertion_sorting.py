"""
Unit tests for the selection_sort and selection_sort_recursive functions.
This module uses Python's unittest framework to verify the correctness of the recursive
selection sort implementation against Python's built-in sorted() function.
"""
import copy
import unittest

from sorting.base_test_sorting import BaseSortingTest
from sorting.insertion_sort import insertion_sort
from util.function_timer import timer


class InsertionSortTest(BaseSortingTest):
    """
    A test case class that tests the recursive selection sort function using various scenarios.
    """

    @timer
    def sort(self, arr):
        """
        Helper method that copies the input array, sorts it using the recursive selection sort,
        and asserts that the result matches Python’s built-in sorted() output.

        Args:
            arr (list): The input list to sort and test.
        """
        sorted_arr = copy.deepcopy(arr)
        insertion_sort(sorted_arr)
        self.assertEqual(sorted(arr), sorted_arr)


if __name__ == '__main__':
    # Run all unit tests
    #  python -m unittest sorting.test_selection_sorting.InsertionSortTest
    unittest.main()
