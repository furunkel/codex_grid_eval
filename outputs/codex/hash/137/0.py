
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text == '':
        return None
    return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2S hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3') == 'md5'
    """
    if hash == '':
        return None
    return blake2s(bytes.fromhex(hash)).decode('utf-8')


def hash_to_int(hash):
    """
    Given a BLAKE2S hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3') == 16777216
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its BLAKE2S hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(16777216) == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if integer == 0:
        return None
    return hex(integer)[2:]


def hash_to_bytes(hash):
    """
    Given a BLAKE2S hash 'hash', return its bytes equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_bytes('99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e