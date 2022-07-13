
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    return blake2s(text.encode(), digest_size=32)


def hash_to_string(hash):
    """
    Given a BLAKE2S hash string, return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == '0'
    """
    if hash == '':
        return None
    return blake2s(hash.encode(), digest_size=32).hex()


def hash_to_int(hash):
    """
    Given a BLAKE2S hash string, return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == 0
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(i):
    """
    Given an integer 'i', return its BLAKE2S hash equivalent string.
    If 'i' is an empty string, return None.

    >>> int_to_hash(0) == '0'
    """
    if i == 0:
        return None
    return blake2s(hex(i).encode(), digest_size=32).hex()


def int_to_string(i, alphabet=string.printable):
    """
    Given an integer 'i', return its string equivalent.
    If 'i' is an empty string, return None.

    >>> int_to_string(0) == '0'
    """
    if i == 0:
        return None
    return ''.join(alphabet[i % len(alphabet)]
                   for i in range(int(i)))


def int_to_bytes(i):
    """
    Given an integer 'i', return its bytes equivalent.
    If 'i' is an empty string, return None.

    >>> int_to_bytes(0) == b'\x00'
    """
    if i == 0:
        return None
    return bytes(int(i), 'ascii')


def bytes_to_int(b):
    """
    Given a bytes 'b', return its integer equivalent.
    If 'b' is an empty string, return None.

    >>> bytes_to_int(b'\x00') == 0
    """
    if b == b'':
        return None
    return int(b.decode('ascii'), 16)


def bytes_to_string(b):
    """
    Given a bytes 'b', return its string equivalent.
    If 'b' is an empty string, return None.

    >>> bytes_to_string(b'\x00') == '0'
    """
    if b == b'':
        return None
    return b.decode('ascii')


def bytes_to_hash(b):
    """