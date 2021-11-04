import timerutil
import logger
from power import power_recursion


def binary_converter(num, index, result):
    val = power_recursion(2, index)
    if num > val:
        binary_converter(num, index + 1, result)
    elif num == val:
        result.append(index)
    else:
        result.append(index - 1)
        new_val = num - power_recursion(2, index - 1)
        binary_converter(new_val, 0, result)


def print_binary_complex(num):
    result = []
    if num <= 1:
        return num
    binary_converter(num, 0, result)
    binary_number = 0
    for i in result:
        binary_number += power_recursion(10, i)
    return binary_number


def binary_helper(num, result):
    if num <= 1:
        result.append(num)
    else:
        if num % 2 == 0:
            result.append(0)
        else:
            result.append(1)
        num = int(num/2)
        binary_helper(num, result)


def print_binary(num):
    result = []
    binary_helper(num, result)
    if len(result) == 1:
        return result[0]
    binary_number = ""
    for i in range(0, len(result)):
        binary_number += str(result.pop())
    return binary_number

if __name__ == "__main__":
    logger.info(print_binary(2123242354325))

