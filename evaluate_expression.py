import timerutil
import logger


class Tracker:
    def __init__(self):
        self.index = 0

    def increment_index(self):
        self.index += 1

    def reset_index(self):
        self.index = 0


def evaluate_exp(expr, tracker):
    my_char = expr[tracker.index]
    if my_char == "(":
        tracker.increment_index()
        left = evaluate_exp(expr, tracker)
        operator = expr[tracker.index]
        tracker.increment_index()
        right = evaluate_exp(expr, tracker)
        tracker.increment_index()
    else:
        tracker.increment_index()
        return int(my_char)

    if operator == "+":
        return left + right
    else:
        return left * right


if __name__ == "__main__":
    tracker = Tracker()
    # print(evaluate_exp("7"))
    # print(evaluate_exp("(2+2)"))
    print(evaluate_exp("(1+(2*4))", tracker))
    tracker.reset_index()
    print(evaluate_exp("((1+3)+((1+2)*5))", tracker))
