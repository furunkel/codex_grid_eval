def find_char_long(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20]


def find_char_short(text):
    """
    Finds all words which are at least 20 characters short in a string.
    """
    return [i for i in range(0, len(text)) if len(text) <= 20]


def find_char_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20]


def find_char_not_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) <= 20]


def find_char_not_space_or_tab(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20 and text[i] != ' ' and text[i] != '\t']


def find_char_not_tab(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20 and text[i] != '\t']


def find_char_not_tab_or_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20 and text[i] != '\t']


def find_char_not_space_or_tab_or_space(text):
    """
    Finds all words which are at least 20 characters long in a string.
    """
    return [i for i in range(0, len(text)) if len(text) >= 20 and text[i] != '\t']


def find_char_not_space_or_tab_or_space_or_tab(text