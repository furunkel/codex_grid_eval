
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.

    >>> hash_to_string('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == '0'
    """
    if hash is None:
        return ''
    return blake2s(bytes.fromhex(hash)).hexdigest()


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is None, return 0.

    >>> hash_to_int('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == 0
    """
    if hash is None:
        return 0
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(0) == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if integer == 0:
        return None
    return blake2s(integer.to_bytes(32, 'big')).hexdigest()


def hash_to_bytes(hash):
    """
    Given a hash 'hash', return its bytes equivalent.
    If 'hash' is None, return b'\x00' * 32.

    >>> hash_to_bytes('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == b'\x00' * 32
    """
   