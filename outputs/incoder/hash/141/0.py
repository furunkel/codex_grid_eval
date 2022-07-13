
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=32).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=32).hex().upper()


def string_to_hash_hex_long(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=32).hex().upper()


def string_to_hash_hex_long_long(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=64).hex().upper()


def string_to_hash_hex_long_long_long(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long_long('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=128).hex().upper()


def string_to_hash_hex_long_long_long_long(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long_long_long('0'