
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex_int(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_int('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('sha1', 8) == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()[:length]


def string_to_hash_hex_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_int('sha1', 8) == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()[:length]


def string_to_hash_hex(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1', 8) == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':