import logging

logging.basicConfig(filename='execution.log', format="%(asctime)s [%(levelname)-s]: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8', level=logging.DEBUG)


def is_console_on():
    return True


def info(data):
    logging.info(data)
    if is_console_on():
        print(data)


def debug(data):
    logging.debug(data)
    if is_console_on():
        print(data)


def error(data):
    logging.debug(data)
    if is_console_on():
        print(data)
