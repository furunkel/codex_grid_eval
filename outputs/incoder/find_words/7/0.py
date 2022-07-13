
def find_char_long(text):
    """
    Finds all words which are not 3 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) > 3:
            longwords.append(word)
    return longwords


def find_char_short(text):
    """
    Finds all words which are 3 characters long in a string.
    """
    shortwords = []
    for word in text.split():
        if len(word) == 3:
            shortwords.append(word)
    return shortwords


def find_char_all(text):
    """
    Finds all words which are 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) == 3 or len(word) == 4:
            allwords.append(word)
    return allwords


def find_char_all_long(text):
    """
    Finds all words which are not 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) > 3 or len(word) > 4:
            allwords.append(word)
    return allwords


def find_char_all_short(text):
    """
    Finds all words which are 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) == 3 or len(word) == 4:
            allwords.append(word)
    return allwords


def find_char_all_longer(text):
    """
    Finds all words which are not 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) < 3 or len(word) < 4:
            allwords.append(word)
    return allwords


def find_char_all_shorter(text):
    """
    Finds all words which are 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) == 3 or len(word) == 4:
            allwords.append(word)
    return allwords


def find_char_all_longer_short(text):
    """
    Finds all words which are not 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) > 3 or len(word) < 4:
            allwords.append(word)
    return allwords


def find_char_all_longer_long(text):
    """
    Finds all words which are not 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) > 3 or len(word) > 4:
            allwords.append(word)
    return allwords


def find_char_all_shorter_short(text):
    """
    Finds all words which are 3 or 4 characters long in a string.
    """
    allwords = []
    for word in text.split():
        if len(word) == 3 or len(word) == 4:
            