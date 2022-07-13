
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text.encode(), digest_size=32).hexdigest()
    return None


def string_to_hash_hex(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text.encode(), digest_size=32).hex()
    return None


def string_to_hash_hex_long(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text.encode(), digest_size=64).hex()
    return None


def string_to_hash_hex_long_long(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text.encode(), digest_size=128).hex()
    return None


def string_to_hash_hex_long_long_long(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long_long('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text:
        return blake2s(text.encode(), digest_size=256).hex()
    return None


def string_to_hash_hex_long_long_long_long(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_long_long_long_long('md5') == '99684e4a541d50