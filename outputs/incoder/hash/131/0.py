
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32)


def string_to_hash_hex(text):
    """
    Given a string 'text', return its blake2s hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its blake2s hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('md5') == 'Zm9vYmFyZ2V0LzE='
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32).hexdigest()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its blake2s hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('md5') == 'Zm9vYmFyZ2V0LzE='
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32).hexdigest().upper()


def string_to_hash_base64_utf8(text):
    """
    Given a string 'text', return its blake2s hash equivalent base64 utf8 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8('md5') == 'Zm9vYmFyZ2V0LzE='
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32).hexdigest().decode('utf8')


def string_to_hash_base64_utf8_hex(text):
    """
    Given a string 'text', return its blake2s hash equivalent base64 utf8 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8_hex('md5') == 'Zm9vYmFyZ2V0LzE='
    """
    if text == '':
        return None
    return blake2s(text, digest_size=32).hexdigest().decode('utf8').upper()


def string_to_hash_base64_utf8_utf8(text):
    """
    Given a string 'text', return its blake2s hash 