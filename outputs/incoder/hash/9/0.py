
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    return md5(text).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its MD5 hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 0
    """
    if text == '':
        return None
    return int(md5(text).hexdigest(), 16)


def hash_int(hash_str):
    """
    Given an MD5 hash string, return its integer equivalent. If 'hash_str' is
    an empty string, return None.

    >>> hash_int('cfcd208495d565ef66e7dff9f98764da') == 0
    """
    if hash_str == '':
        return None
    return int(hash_str, 16)


def hash_str(hash_int):
    """
    Given an integer, return its MD5 hash equivalent string. If 'hash_int' is
    None, return an empty string.

    >>> hash_str(0) == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if hash_int is None:
        return ''
    return md5(str(hash_int)).hexdigest()


def hash_str_int(hash_str):
    """
    Given an MD5 hash string, return its integer equivalent. If 'hash_str' is
    None, return None.

    >>> hash_str_int('cfcd208495d565ef66e7dff9f98764da') == 0
    """
    if hash_str == '':
        return None
    return int(hash_str, 16)


def hash_str_str(hash_str):
    """
    Given an MD5 hash string, return its string equivalent. If 'hash_str' is
    None, return None.

    >>> hash_str_str('cfcd208495d565ef66e7dff9f98764da') == ''
    """
    if hash_str == '':
        return None
    return hash_str


def hash_str_str_int(hash_str):
    """
    Given an MD5 hash string, return its string and integer equivalents.
    If 'hash_str' is None, return None.

    >>> hash_str_str_int('cfcd208495d565ef66e7dff9f98764da') == ('cfcd208495d565ef66e7dff9f98764da', 0)
    """
    if hash_str == '':
        return None
    return hash_str, int(hash_str, 16)


def hash_str_str_str_int(hash_str):
    """
    Given an MD5 hash string, return its string and string and integer equivalents.
    If 'hash_str' is None, return None.

    >>> hash_str_str_str_int('cfcd208495d565ef66e7