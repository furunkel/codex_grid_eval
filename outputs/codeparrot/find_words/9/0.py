def find_char_long(text):
    """
    Finds all words which are exactly 6 characters long in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isdigit()]


def find_char_short(text):
    """
    Finds all words which are exactly 6 characters short in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha()]


def find_char_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha()]


def find_char_not_in_text_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha()]


def find_char_not_in_text_not_in_text_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha()]


def find_char_not_in_text_not_in_text_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha()]


def find_char_not_in_text_not_in_text_not_in_text(text):
    """
    Finds all words which are not in a string.
    """
    if len(text) < 6:
        return []
    else:
        return [i for i in range(0, len(text)) if text[i].isalpha