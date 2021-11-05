import timerutil
import logger


def permutation_helper(input_str, result):
    if len(input_str) == 0:
        logger.info(result)
    else:
        for x in input_str:
            result = result + x     # Choose
            new_input = input_str.replace(x, "")
            permutation_helper(new_input, result)  # Explore
            result = result[:-1]  # Un-choose


def permutation(input_str):
    permutation_helper(input_str, "")


if __name__ == "__main__":
    permutation("abc")
