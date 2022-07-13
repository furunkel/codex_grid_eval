
def find_char_long(text):
    """
    Finds all words which are not 6 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) > 6:
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


def find_char_middle(text):
    """
    Finds all words which are 2 characters long in a string.
    """
    middlewords = []
    for word in text.split():
        if len(word) == 2:
            middlewords.append(word)
    return middlewords


def find_char_longer(text):
    """
    Finds all words which are 4 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) == 4:
            longwords.append(word)
    return longwords


def find_char_shorter(text):
    """
    Finds all words which are 5 characters long in a string.
    """
    shortwords = []
    for word in text.split():
        if len(word) == 5:
            shortwords.append(word)
    return shortwords


def find_char_middle2(text):
    """
    Finds all words which are 3 characters long in a string.
    """
    middlewords = []
    for word in text.split():
        if len(word) == 3:
            middlewords.append(word)
    return middlewords


def find_char_longer2(text):
    """
    Finds all words which are 4 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) == 4:
            longwords.append(word)
    return longwords


def find_char_shorter2(text):
    """
    Finds all words which are 5 characters long in a string.
    """
    shortwords = []
    for word in text.split():
        if len(word) == 5:
            shortwords.append(word)
    return shortwords


def find_char_middle3(text):
    """
    Finds all words which are 3 characters long in a string.
    """
    middlewords = []
    for word in text.split():
        if len(word) == 3:
            middlewords.append(word)
    return middlewords


def find_char_longer3(text):
    """
    Finds all words which are 4 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) == 4:
            longwords.append(word)
    return longwords


def find_char_shorter3(text):
    """
    Finds all words which are 5 characters long in a string.
    """
    shortwords = []
    for word in text.split():
        if len(word) == 5:
            shortwords.append(word)
    return shortwords


def find_char_middle4(text):
    """
    Finds all words which are 