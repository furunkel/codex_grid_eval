
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_random(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_random_hex(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_hex('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_random_int(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_int('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex_random_int(text):
    """
    Given a string 'text', return its sha-256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_int('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if text == '':
        return None
    return hashlib.sha256(text.