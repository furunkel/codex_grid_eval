
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('0') == 0
    """
    if text == '':
        return None
    return int(text)


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('') == []
    """
    if text == '':
        return None
    return text.split(',')


def string_to_dict(text):
    """
    Given a string 'text', return its dict equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_dict('') == {}
    """
    if text == '':
        return None
    return dict(text.split('='))


def string_to_set(text):
    """
    Given a string 'text', return its set equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_set('') == set()
    """
    if text == '':
        return None
    return set(text.split('='))


def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('') == False
    """
    if text == '':
        return None
    return text.lower() in ['true', '1', 'yes', 'on']


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('') == []
    """
    if text == '':
        return None
    return text.split(',')


def string_to_dict(text):
    """
    Given a string 'text', return its dict equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_dict('') == {}
    """
    if text == '':
        return None
    return dict(text.split('='))


def string_to_set(text):
    """
    Given a string 'text', return its set equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_set('') == set()
    """
    if text == '':
        return None
    return set(text.split('='))


def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('') == False
    """
    if text == '':
        return None
    return text.lower() in ['true', '1', 'yes', 'on']


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 