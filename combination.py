import math
import copy
import unittest


def combination(input_list, r, partial_result, final_result):
    if len(partial_result) == r:
        final_result.append(copy.deepcopy(partial_result))
    else:
        for i in range(len(input_list)):
            partial_result.append(input_list[i])
            combination(input_list[i+1:], r, partial_result, final_result)
            partial_result.pop()
    return final_result


def combination_alt(input_list, r, i, partial_result, final_result):
    if (len(partial_result) + len(input_list)) < r:
        return final_result
    if len(partial_result) == r:
        final_result.append(copy.deepcopy(partial_result))
        return final_result
    elif i == len(input_list):
        return final_result
    else:
        partial_result.append(input_list[i])
        combination_alt(input_list, r, i + 1, partial_result, final_result)
        partial_result.pop()
        combination_alt(input_list, r, i + 1, partial_result, final_result)
    return final_result


def permutation(input_list, r, partial_result, final_result):
    if len(partial_result) == r:
        final_result.append(copy.deepcopy(partial_result))
    else:
        for i in range(len(input_list)):
            partial_result.append(input_list[i])
            new_input_list = copy.deepcopy(input_list)
            new_input_list.pop(i)
            permutation(new_input_list, r, partial_result, final_result)
            partial_result.pop()
    return final_result


def calculate_number_of_combination(n, r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))


def calculate_number_of_permutation(n, r):
    return int(math.factorial(n)/math.factorial(n-r))


def print_divider_line(symbol, no_of_occurrence):
    line = []
    for i in range(no_of_occurrence):
        line.append(symbol)
    print("".join(line))


class TestPermutation(unittest.TestCase):

    def test(self):
        self.assertEqual(len(permutation([1, 2, 3, 4], 3, [], [])), calculate_number_of_permutation(4, 3))


def main():
    unittest.main()
    pass


if __name__ == "__main__":
    main()


