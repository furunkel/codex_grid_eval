
def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if text == '':
        return None
    return sha512(text.encode('utf-8')).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its sha-512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == -449544395
    """
    if text == '':
        return None
    return int(sha512(text).hexdigest(), 16)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha-512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == -449544395
    """
    if text == '':
        return None
    return int(sha512(text.encode('utf-8')).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha-512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == -449544395
    """
    if text == '':
        return None
    return int(sha512(text.encode('utf-8')).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha-512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == -449544395
    """
    if text == '':
        return None
    return int(sha512(text.encode('utf-8')).hexdigest(), base)


def string_to_hash_int(text, base=16):
    """
    Given a string 'text', return its sha-512 hash equivalent int.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('Hello world') == -449544395
    """
    if text == '':
        return None
    return int(sha