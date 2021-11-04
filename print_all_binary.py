import timerutil
import logger


def print_all_binary_helper(digits, result):
    if digits < 1:
        logger.info(result)
        return
    else:
        for i in range(2):
            result = result + str(i)  # Choose
            print_all_binary_helper(digits - 1, result)  # Explore
            result = result[:-1]    # Un-choose


def print_all_binary(digits):
    print_all_binary_helper(digits, "")


if __name__ == "__main__":
    print_all_binary(3)
