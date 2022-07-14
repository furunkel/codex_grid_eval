def find_char_long(text):
    """
    Finds all words which are not 20 characters long in a string.
    """
    return [i for i in re.finditer(r'\d+', text)]


def find_char_short(text):
    """
    Finds all words which are not 20 characters short in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long(text):
    """
    Finds all words which are not 20 characters long in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_short(text):
    """
    Finds all words which are not 20 characters short in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short(text):
    """
    Finds all words which are not 20 characters long or short in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short_or_space(text):
    """
    Finds all words which are not 20 characters long or short or space in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short_or_space(text):
    """
    Finds all words which are not 20 characters long or short or space in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short_or_space_or_not_space(text):
    """
    Finds all words which are not 20 characters long or short or space or not space in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short_or_space_or_not_space(text):
    """
    Finds all words which are not 20 characters long or short or space or not space in a string.
    """
    return [i for i in re.finditer(r'\w+', text)]


def find_char_not_long_or_short