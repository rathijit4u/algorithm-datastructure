import copy
import unittest


class ArraySum:
    def __init__(self, k):
        self.k = k
        self.results = []

    def sum_of_elements(self, input_array):
        input_array.sort()
        if len(self.results) > 0:
            self.results.clear()
        self.sum_of_elements_helper(input_array, [])
        return self.results

    def sum_of_elements_helper(self, input_array, partial_result):
        if sum(partial_result) == self.k and partial_result not in self.results:
            self.results.append(copy.deepcopy(partial_result))
        else:
            for i in range(0, len(input_array)):
                partial_result.append(input_array[i])
                self.sum_of_elements_helper(input_array[i+1:], partial_result)
                partial_result.pop()


class TestArraySum(unittest.TestCase):

    def test(self):
        k = 8
        input_arr = [1, 5, 3, 2, 6]
        array_sum = ArraySum(k)

        self.assertEqual([[1, 2, 5], [2, 6], [3, 5]], array_sum.sum_of_elements(input_arr))


def main():
    k = 8
    array_sum = ArraySum(k)
    print(array_sum.sum_of_elements([10, 1, 2, 7, 6, 1, 5]))
    unittest.main()
    pass


if __name__ == "__main__":
    main()
