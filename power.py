import timerutil
import logger


def calculate_power_recursion(base, exp):
    if exp == 0:
        return 1
    else:
        if exp % 2 == 0:
            return calculate_power_recursion(base*base, exp/2)
        else:
            return calculate_power_recursion(base, exp - 1) * base


def calculate_power_recursion_non_optimized(base, exp):
    if exp == 0:
        return 1
    else:
        return calculate_power_recursion_non_optimized(base, exp - 1) * base


def power_recursion(base, exp, is_optimized=True):
    timer = timerutil.TimerUtil()
    if exp < 0:
        new_exp = -1 * exp
    else:
        new_exp = exp

    if is_optimized:
        temp_result = calculate_power_recursion(base, new_exp)
    else:
        temp_result = calculate_power_recursion_non_optimized(base, new_exp)
    timer.stop_timer()
    if exp < 0:
        return 1 / temp_result
    else:
        return temp_result


def calculate_power_loop(base, exp):
    if exp == 0:
        return 1
    else:
        temp_result = 1
        for i in range(0, exp):
            temp_result = temp_result * base
        return temp_result


def power_loop(base, exp):
    timer = timerutil.TimerUtil()
    temp_result = None
    if exp < 0:
        exp = -1 * exp
        temp_result = 1 / calculate_power_loop(base, exp)
    else:
        temp_result = calculate_power_loop(base, exp)
    timer.stop_timer()
    return temp_result


if __name__ == "__main__":
    base_number, exponent = 3, 0
    result = power_recursion(base_number, exponent, True)
    logger.info(result)
    result = power_loop(base_number, exponent)
    logger.info(result)
