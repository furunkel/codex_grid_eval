
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def blake2s(data):
    """
    Given a binary string 'data', return a binary string equivalent to
    the blake2s hash function of 'data'.
    If 'data' is an empty string, return None.

    >>> blake2s('abc') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    """
    if data == '':
        return None
    return blake2s_update(data)


def blake2s_update(data):
    """
    Given a binary string 'data', return a binary string equivalent to
    the blake2s hash function of 'data'.
    If 'data' is an empty string, return None.

    >>> blake2s_update('abc') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    """
    length = len(data)
    length_bytes = length.to_bytes(8, 'big')
    length_bytes = length_bytes.ljust(8, b'\x00')
    length_int = int.from_bytes(length_bytes, 'big')
    hash_data = length_int + data
    return blake2s(hash_data)


def blake2s_digest(data):
    """
    Given a binary string 'data', return a binary string equivalent to
    the blake2s hash function of 'data'.
    If 'data' is an empty string, return None.

    >>> blake2s_digest('abc') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    """
    if data == '':
        return None
    return blake2s(data).hexdigest()


def blake2s_checksum(data):
    """
    Given a binary string 'data', return a binary string equivalent to
    the blake2s hash function of 'data'.
    If 'data' is an empty string, return None.

    >>> blake2s_checksum('abc') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
    """
    if data == '':
        return None
    return blake2s(data).digest()


def blake2s_checksum_hexdigest(data):
    """
    Given a binary string 'data', return a 