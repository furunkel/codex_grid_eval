def find_char_long(text):
    """
    Finds all words which are at most 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "0123456789"]


def find_char_short(text):
    """
    Finds all words which are at least 3 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_space(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\n\r\v\f"]


def find_char_not_space(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\r\f\v\f"]


def find_char_not_space_or_tab(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\r\f\v\f"]


def find_char_not_tab(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\r\f\v\f"]


def find_char_not_tab_or_space(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\r\f\v\f"]


def find_char_not_tab_or_tab_or_space_or_tab(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in " \t\r\f\v\