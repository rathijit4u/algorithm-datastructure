import logger


def write_text(file_name, text):
    try:
        with open(file_name, "w") as file:
            file.write(str(text))
    except IOError as e:
        logger.error("Error. {0}".format(e))


def write(file_name, data):
    write_text(file_name, str(data))