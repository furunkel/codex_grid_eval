
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text, digest_size=32)
    return None


def hash_to_string(hash):
    """
    Given a blake2s hash string, return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3') == 'md5'
    """
    if hash:
        return blake2s(hash, digest_size=32).hexdigest()
    return None


def hash_to_int(hash):
    """
    Given a blake2s hash string, return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3') == 1357799410
    """
    if hash:
        return int(hash, 16)
    return None


def int_to_hash(n):
    """
    Given an integer 'n', return its blake2s hash equivalent string.
    If 'n' is None, return None.

    >>> int_to_hash(1357799410) == 'md5'
    """
    if n:
        return blake2s(n, digest_size=32).hexdigest()
    return None


def int_to_string(i, alphabet=string.ascii_lowercase, length=8):
    """
    Given an integer 'i', return its string equivalent in 'alphabet'.
    If 'i' is None, return None.

    >>> int_to_string(1357799410) == 'md5'
    """
    if i:
        return ''.join(alphabet[i % len(alphabet)]
                       for i in range(length))
    return None


def string_to_int(text, alphabet=string.ascii_lowercase, length=8):
    """
    Given a string 'text', return its integer equivalent in 'alphabet'.
    If 'text' is an empty string, return None.

    >>> string_to_int('md5') == 1357799410
    """
    if text:
        return int(text, 16)
    return None


def int_to_bytes(i, alphabet=string.ascii_lowercase, length=8):
    """
    Given an integer 'i', return its bytes equivalent in 'alphabet'.
    If 'i' is None, return None.

    >>> int_to_bytes(1357799410) == b'md5'
    """
    if i:
        return bytes(alphabet[i % len(alphabet)]
                    for i in range(length))
    return None


def bytes_to_int(b, alphabet=string.ascii_lowercase, length=8):
    """
    Given a bytes 'b', return its 