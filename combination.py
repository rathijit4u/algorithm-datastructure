import math
import copy


def combination(input_list, r, partial_result, final_result):
    if len(partial_result) == r:
        final_result.append(copy.deepcopy(partial_result))
    else:
        for i in range(len(input_list)):
            partial_result.append(input_list[i])
            combination(input_list[i+1:], r, partial_result, final_result)
            partial_result.pop()
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

input_value = [1, 2, 3]
print(calculate_number_of_permutation(len(input_value), 3))
print(calculate_number_of_combination(len(input_value), 3))
print(combination(input_value, 3, [], []))
print("===============================")
print(permutation(input_value, 3, [], []))

