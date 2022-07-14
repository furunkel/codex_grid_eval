def find_char_long(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in string.ascii_letters]


def find_char_short(text):
    """
    Finds all words which are not 3 characters short in a string.
    """
    return [i for i in range(0, len(text)) if text[i] not in string.ascii_letters]


def find_char_mixed(text):
    """
    Finds all words which are not 3 characters mixed in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in string.ascii_letters and i not in string.ascii_letters]


def find_char_mixed_long(text):
    """
    Finds all words which are not 3 characters mixed in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters]


def find_char_mixed_short(text):
    """
    Finds all words which are not 3 characters mixed in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters]


def find_char_mixed_long_long(text):
    """
    Finds all words which are not 3 characters mixed in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters]


def find_char_mixed_short_long(text):
    """
    Finds all words which are not 3 characters mixed in a string.
    """
    return [i for i in range(0, len(text)) if text[i] in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters and i not in string.ascii_letters]


def find_char_mixed_