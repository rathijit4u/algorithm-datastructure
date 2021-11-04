import timerutil
import logger


def reverse_lines(lines):
    if len(lines) == 0:
        return
    else:
        logger.info(lines[-1])
        reverse_lines(lines[:-1])


if __name__ == "__main__":
    try:
        with open("test.txt", "r") as file:
            file_lines = file.readlines()
            reverse_lines(file_lines)
    except IOError as e:
        logger.error(e)

