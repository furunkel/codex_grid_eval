
def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex_random(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex_random_hex(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_hex('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex_random_int(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_int('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex_random_int(text):
    """
    Given a string 'text', return its sha-224 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_random_int('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return sha224(text).hexdigest()


def string_to_hash_hex_random_int(text):
    """
    Given a string 'text', 