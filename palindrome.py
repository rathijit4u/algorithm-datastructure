import timerutil
import logger


def is_palindrome(word):
    word = word.lower()
    word_length = len(word)
    if word_length <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:(word_length - 1)])
    else:
        return False


if __name__ == "__main__":
    logger.info(is_palindrome("m aam"))
