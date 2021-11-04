import timerutil
import logger


def print_all_hexadecimal_helper(digits, result):
    if digits < 1:
        logger.info(result)
        return
    else:
        for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
            result = result + i  # Choose
            print_all_hexadecimal_helper(digits - 1, result)  # Explore
            result = result[:-1]    # Un-choose


def print_all_hexadecimal(digits):
    print_all_hexadecimal_helper(digits, "")


if __name__ == "__main__":
    print_all_hexadecimal(2)
