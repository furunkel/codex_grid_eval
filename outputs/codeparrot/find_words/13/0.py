def find_char_long(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] == ' ' and len(text[i + 1]) == 20]


def find_char_short(text):
    """
    Finds all words which are exactly 20 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] == ' ' and len(text[i + 1]) == 20]


def find_char_space(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] == ' ' and len(text[i + 1]) == 20]


def find_char_not_space(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and len(text[i + 1]) != 20]


def find_char_not_space_or_tab(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and len(text[i + 1]) != 20]


def find_char_not_space_or_tab_or_space(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and len(text[i + 1]) != 20]


def find_char_not_space_or_tab_or_space_or_tab(text):
    """
    Finds all words which are exactly 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] != ' ' and len(text[i + 1]) != 20]


def find_char_not_space_or_tab_or_space_or_tab_or_space(text):
    """
    Finds all