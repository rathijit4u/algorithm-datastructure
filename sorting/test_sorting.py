"""
Unit tests for the selection_sort and selection_sort_recursive functions.
This module uses Python's unittest framework to verify the correctness of the recursive
selection sort implementation against Python's built-in sorted() function.
"""


import unittest
import random
from selection_sort import selection_sort, selection_sort_recursive

class SortingTest(unittest.TestCase):
    """
    A test case class that tests the recursive selection sort function using various scenarios.
    """

    def helper(self, arr):
        """
        Helper method that copies the input array, sorts it using the recursive selection sort,
        and asserts that the result matches Python’s built-in sorted() output.

        Args:
            arr (list): The input list to sort and test.
        """
        sorted_arr = arr.copy()
        selection_sort_recursive(sorted_arr, len(sorted_arr))
        self.assertEqual(sorted(arr), sorted_arr)

    def test_sorting_1(self):
        """Test sorting a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.helper(arr)

    def test_sorting_2(self):
        """Test sorting a list with a single element."""
        arr = [1]
        self.helper(arr)

    def test_sorting_3(self):
        """Test sorting an empty list."""
        arr = []
        self.helper(arr)

    def test_sorting_4(self):
        """Test sorting a list with all equal elements."""
        arr = [1,1,1,1,1]
        self.helper(arr)

    def test_sorting_5(self):
        """Test sorting a list with both positive and negative duplicate values."""
        arr = [1,-1,1,1,-1,1]
        self.helper(arr)

    def test_sorting_6(self):
        """Test sorting a list with mixed duplicates and negative numbers."""
        arr = [-2,-1,1,1,-1,-2]
        self.helper(arr)

    def test_sorting_7(self):
        """Test sorting an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.helper(arr)

    def test_sorting_8(self):
        """Test sorting a list of floating point numbers."""
        arr = [3.2, 1.5, 4.8, 1.1]
        self.helper(arr)

    def test_sorting_9(self):
        """Test sorting a list of floating point numbers."""
        arr = list(range(1000))
        random.shuffle(arr)
        self.helper(arr)

    def test_sorting_10(self):
        """Test sorting a list of strings."""
        arr = ["banana", "apple", "cherry"]
        self.helper(arr)

if __name__ == '__main__':
    # Run all unit tests
    unittest.main()
