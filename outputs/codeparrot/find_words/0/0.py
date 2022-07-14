def find_char_long(text):
    """
    Finds all words which are at least 1 characters long in a string.
    """
    return [i for i in range(len(text)) if text[i].isdigit()]


def find_char_short(text):
    """
    Finds all words which are at least 1 characters short in a string.
    """
    return [i for i in range(len(text)) if text[i].isalpha()]


def find_char_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    return [i for i in range(len(text)) if text[i] not in string.punctuation]


def find_char_not_in_text_and_not_in_text(text):
    """
    Finds all words which are not in a string and not in a string.
    """
    return [i for i in range(len(text)) if text[i] not in string.punctuation and not text[i].isalpha()]


def find_char_not_in_text_and_not_in_text_and_not_in_text(text):
    """
    Finds all words which are not in a string and not in a string.
    """
    return [i for i in range(len(text)) if text[i] not in string.punctuation and not text[i].isalpha()]


def find_char_not_in_text_and_not_in_text_and_not_in_text(text):
    """
    Finds all words which are not in a string and not in a string.
    """
    return [i for i in range(len(text)) if text[i] not in string.punctuation and not text[i].isalpha()]


def find_char_not_in_text_and_not_in_text_and_not_in_text(text):
    """
    Finds all words which are not in a string and not in a string.
    """
    return [i for i in range(len(text)) if text[i] not in string.punctuation and not text[i].isalpha()]


def find_char_not_in_text_and_not_in_text_and_not_in_text(text):
    """
    Finds