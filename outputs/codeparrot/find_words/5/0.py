def find_char_long(text):
    """
    Finds all words which are exactly 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] == ' ' and i < len(text) - 1]


def find_char_short(text):
    """
    Finds all words which are exactly 3 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] == ' ' and i > 0]


def find_char_not_long(text):
    """
    Finds all words which are exactly 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and i > 0]


def find_char_not_short(text):
    """
    Finds all words which are exactly 3 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and i > 0]


def find_char_not_long_or_short(text):
    """
    Finds all words which are exactly 3 characters long or short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and i > 0 and text[i - 1] != ' ' and i < len(text) - 1]


def find_char_not_long_or_short_or_space(text):
    """
    Finds all words which are exactly 3 characters long or short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and i > 0 and text[i - 1] != ' ' and i < len(text) - 1 and text[i + 1] != ' ' and i < len(text) - 1]


def find_char_not_long_or_short_or_space_or_not_space(text):
    """
    Finds all words which are exactly 3 characters long or short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and i > 0 and text[i - 1] != ' ' and i