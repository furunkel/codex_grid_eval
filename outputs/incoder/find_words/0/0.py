
def find_char_long(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 2:
            chars.append(word)
    return chars


def find_char_short(text):
    """
    Finds all words which are at least 2 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 3:
            chars.append(word)
    return chars


def find_char_medium(text):
    """
    Finds all words which are at least 3 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 4:
            chars.append(word)
    return chars


def find_char_longer(text):
    """
    Finds all words which are at least 4 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 5:
            chars.append(word)
    return chars


def find_char_shorter(text):
    """
    Finds all words which are at least 5 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 6:
            chars.append(word)
    return chars


def find_char_longer_or_shorter(text):
    """
    Finds all words which are at least 6 characters long or at least 3 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 6:
            chars.append(word)
        elif len(word) > 3:
            chars.append(word)
    return chars


def find_char_longer_or_shorter_or_medium(text):
    """
    Finds all words which are at least 6 characters long or at least 4 characters long or at least 3 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 6:
            chars.append(word)
        elif len(word) > 4:
            chars.append(word)
        elif len(word) > 3:
            chars.append(word)
    return chars


def find_char_longer_or_shorter_or_medium_or_longer(text):
    """
    Finds all words which are at least 6 characters long or at least 4 characters long or at least 3 characters long or at least 5 characters long in a string.
    """
    chars = []
    for word in text.split():
        if len(word) > 6:
            chars.append(word)
        elif len(word) > 4:
            chars.append(word)
        elif len(word) > 3:
            chars.append(word)
        elif len(word) > 5:
            chars.append(word)
    return chars


def find_char_longer_or_shorter_or_medium_or_longer_or_shorter(text):
    """
    Finds all words which are at least 6 characters long or at least 4 characters long or at least 3 characters long or at least 5 characters long or at least 6 characters long in a string.
    """
    chars = []
