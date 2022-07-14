def find_char_long(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "0123456789"]


def find_char_short(text):
    """
    Finds all words which are at most 6 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_space(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\n\r\v\f"]


def find_char_not_space(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in " \t\r\v\f"]


def find_char_not_word(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in " \t\r\v\f"]


def find_char_not_word_or_space(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in " \t\r\v\f"]


def find_char_not_word_or_space_or_not_word(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in " \t\r\v\f"]


def find_char_not_word_or_space_or_not_word_or_not_space(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in " \t