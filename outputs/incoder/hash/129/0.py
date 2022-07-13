
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_to_string(hash):
    """
    Given a blake2s hash string, return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == '0'
    """
    if hash == '':
        return None
    return blake2s(hash.encode()).hexdigest()


def hash_to_int(hash):
    """
    Given a blake2s hash string, return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == 0
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(num):
    """
    Given an integer 'num', return its blake2s hash equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_hash(0) == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if num == 0:
        return None
    return blake2s(num.to_bytes(32, byteorder='big')).hexdigest()


def int_to_string(num):
    """
    Given an integer 'num', return its string equivalent.
    If 'num' is an empty string, return None.

    >>> int_to_string(0) == '0'
    """
    if num == 0:
        return None
    return num.to_bytes(32, byteorder='big').hex()


def int_to_bytes(num):
    """
    Given an integer 'num', return a byte string equivalent of it.
    If 'num' is an empty string, return None.

    >>> int_to_bytes(0) == b'\x00'
    """
    if num == 0:
        return None
    return num.to_bytes(32, byteorder='big')


def bytes_to_int(b):
    """
    Given a byte string 'b', return its integer equivalent.
    If 'b' is an empty string, return None.

    >>> bytes_to_int(b'\x00') == 0
    """
    if b == '':
        return None
    return int(b, 16)


def bytes_to_string(b):
    """
    Given a byte string 'b', return its string equivalent.
    If 'b' is an empty string, return None.

    >>> bytes_to_string(b'\x00') == '0'
    """
