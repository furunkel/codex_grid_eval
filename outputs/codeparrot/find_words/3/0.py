def find_char_long(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_short(text):
    """
    Finds all words which are not 1 characters short in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_long(text):
    """
    Finds all words which are not 1 characters long in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_short(text):
    """
    Finds all words which are not 1 characters short in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_long_or_short(text):
    """
    Finds all words which are not 1 characters long or short in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_long_or_short_or_space(text):
    """
    Finds all words which are not 1 characters long or short or space in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_long_or_short_or_space_or_blank(text):
    """
    Finds all words which are not 1 characters long or short or space or blank in a string.
    """
    if len(text) < 1:
        return []
    return [i for i in range(len(text)) if text[i] != ' ']


def find_char_not_long_or_short_or_space_or_blank_or_space(text):
    """
    Finds all