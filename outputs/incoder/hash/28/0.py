
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA1 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its SHA1 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex_base64(text):
    """
    Given a string 'text', return its SHA1 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its SHA1 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex_base64_hex(text):
    """
    Given a string 'text', return its SHA1 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64_hex('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex_base64_base64(text):
    """
    Given a string 'text', return its SHA1 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_base64_base64('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48