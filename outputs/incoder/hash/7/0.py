
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_int(text, base=10):
    """
    Given a string 'text', return its integer equivalent in base 'base'.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hello world') == 12
    """
    if text == '':
        return None
    return int(text, base)


def string_to_list(text):
    """
    Given a string 'text', return a list of its characters. Empty string
    returns an empty list.

    >>> string_to_list('Hello world') == ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    """
    if text == '':
        return []
    return list(text)


def string_to_set(text):
    """
    Given a string 'text', return a set of its characters. Empty string
    returns an empty set.

    >>> string_to_set('Hello world') == {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'}
    """
    if text == '':
        return set()
    return set(text)


def string_to_tuple(text):
    """
    Given a string 'text', return a tuple of its characters. Empty string
    returns an empty tuple.

    >>> string_to_tuple('Hello world') == ('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
    """
    if text == '':
        return tuple()
    return tuple(text)


def string_to_dict(text):
    """
    Given a string 'text', return a dict whose keys are its characters. Empty
    string returns an empty dict.

    >>> string_to_dict('Hello world') == {'H': 'e', 'e': 'l', 'l': 'l', 'o': '', ' ': 'w', 'w': 'o', 'r': 'l', 'd': ''}
    """
    if text == '':
        return dict()
    return dict(zip(list(text), list(text)))


def string_to_bool(text):
    """
    Given a string 'text', return a boolean whose value is True if 'text' is
    not an empty string and False otherwise. Empty string returns False.

    >>> string_to_bool('Hello world') == True
    """
    if text == '':
        return False
    return bool(text)


def string_to_list(text, separator=','):
    """
    Given a string 'text', return a list whose values are the characters of
    'text' separated by 'separator'. Empty string returns an empty list.

    >>> string_to_list('Hello world') == ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    """
    if text == '':
        return []
    return text.split(separator)


def string_to_set(text, separator=','):
    """
    Given a string 'text', return a set whose values are the 