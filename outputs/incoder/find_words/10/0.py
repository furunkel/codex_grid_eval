
def find_char_long(text):
    """
    Finds all words which are at most 6 characters long in a string.
    """
    longwords = []
    for word in text.split():
        if len(word) > 6:
            longwords.append(word)
    return longwords


def find_char_short(text):
    """
    Finds all words which are at most 3 characters long in a string.
    """
    shortwords = []
    for word in text.split():
        if len(word) > 3:
            shortwords.append(word)
    return shortwords


def find_char_common(text):
    """
    Finds all words which are common to at least 3 strings.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            commonwords.append(word)
    return commonwords


def find_char_common_long(text):
    """
    Finds all words which are common to at least 3 strings and are at most 6 characters long.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) > 6:
                commonwords.append(word)
    return commonwords


def find_char_common_short(text):
    """
    Finds all words which are common to at least 3 strings and are at most 3 characters long.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) > 3:
                commonwords.append(word)
    return commonwords


def find_char_common_longer(text):
    """
    Finds all words which are common to at least 3 strings and are longer than 3 characters.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) > 3:
                commonwords.append(word)
    return commonwords


def find_char_common_shorter(text):
    """
    Finds all words which are common to at least 3 strings and are shorter than 3 characters.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) < 3:
                commonwords.append(word)
    return commonwords


def find_char_common_longer_shorter(text):
    """
    Finds all words which are common to at least 3 strings and are longer than 3 characters and shorter than 3 characters.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) > 3 and len(word) < 6:
                commonwords.append(word)
    return commonwords


def find_char_common_longer_longer(text):
    """
    Finds all words which are common to at least 3 strings and are longer than 3 characters and longer than 3 characters.
    """
    commonwords = []
    for word in text.split():
        if word in commonwords:
            pass
        else:
            if len(word) > 3 and 