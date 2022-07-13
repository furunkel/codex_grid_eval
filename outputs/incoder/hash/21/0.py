
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha1 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its sha1 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return int(sha1(text).hexdigest(), 16)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha1 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return int(sha1(text).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha1 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return int(sha1(text).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha1 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return int(sha1(text).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha1 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
