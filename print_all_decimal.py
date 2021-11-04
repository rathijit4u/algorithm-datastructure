import timerutil
import logger


def print_all_decimal_helper(digits, result):
    if digits < 1:
        logger.info(result)
        return
    else:
        for i in range(10):
            result = result + str(i)
            print_all_decimal_helper(digits - 1, result)
            result = result[:-1]


def print_all_decimal(digits):
    print_all_decimal_helper(digits, "")


if __name__ == "__main__":
    print_all_decimal(4)
