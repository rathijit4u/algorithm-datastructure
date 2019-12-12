from combination import *


input_value = [3, 2, 5, 8, 83, 43, 56, 99, 50, 832, 867, 12, 346, 958, 754, 42342, 327429, 574, 343, 434, 554, 77439, 433202, 75454]
input_value = [3, 2, 5, 8]
pick = 3
print(calculate_number_of_permutation(len(input_value), pick))
# print(calculate_number_of_combination(len(input_value), pick))
# print(combination(input_value, pick, [], []))
#
# print_divider_line("=", calculate_number_of_combination(len(input_value), pick) * pick)
# print(permutation(input_value, pick, [], []))
# print_divider_line("=", calculate_number_of_combination(len(input_value), pick) * pick)
# print(combination_alt(input_value, pick, 0, [], []))
print(calculate_number_of_permutation(28, 2))
