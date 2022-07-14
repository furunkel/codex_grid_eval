def find_char_long(text):
    """
    Finds all words which are at most 1 characters long in a string.
    """
    return [i for i in range(len(text)) if text[i] in "0123456789"]


def find_char_short(text):
    """
    Finds all words which are at least 1 characters short in a string.
    """
    return [i for i in range(len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long(text):
    """
    Finds all words which are at most 1 characters long in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "0123456789"]


def find_char_not_short(text):
    """
    Finds all words which are at least 1 characters short in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long_or_short(text):
    """
    Finds all words which are at least 1 characters long or short in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long_or_short_or_space(text):
    """
    Finds all words which are at least 1 characters long or short in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long_or_short_or_space_or_blank(text):
    """
    Finds all words which are at least 1 characters long or short in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long_or_short_or_space_or_blank_or_space(text):
    """
    Finds all words which are at least 1 characters long or short in a string.
    """
    return [i for i in range(len(text)) if text[i] not in "abcdefghijklmnopqrstuvwxyz"]


def find_char_not_long_or_short_or_space_or_blank_or_space(text):
    """
   