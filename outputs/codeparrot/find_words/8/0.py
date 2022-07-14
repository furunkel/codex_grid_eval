def find_char_long(text):
    """
    Finds all words which are at least 6 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "0123456789"]


def find_char_short(text):
    """
    Finds all words which are at least 6 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_simple(text):
    """
    Finds all words which are at least 6 characters simple in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_long(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_short(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_long_long(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_short_long(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_long_short(text):
    """
    Finds all words which are at least 6 characters complex in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in "abcdefghijklmnopqrstuvwxyz"]


def find_char_complex_short_short