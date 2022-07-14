def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == '1':
        return None
    return text[1:-1]


def get_hash_from_text(text):
    """
    Given a string 'text', return its hash equivalent string.
    If 'text' is an empty string, return None.

    >>> get_hash_from_text('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == '1':
        return None
    return text[1:-1]


def get_hash_from_file(filename):
    """
    Given a file 'filename', return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_hash_from_file('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    if filename[0] == '0':
        return None
    if filename[-1] == '1':
        return None
    return filename[1:-1]


def get_hash_from_file_with_hash(filename, hash_type=None):
    """
    Given a file 'filename', return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_hash_from_file_with_