
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).hexdigest()
    return None


def string_to_hash_hex(text):
    """
    Given a string 'text', return its blake2b hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).hex()
    return None


def string_to_hash_int(text):
    """
    Given a string 'text', return its blake2b hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -2581084514
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).intdigest()
    return None


def string_to_hash_int(text, hex=False):
    """
    Given a string 'text', return its blake2b hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -2581084514
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).intdigest(hex)
    return None


def string_to_hash_int(text, hex=True, bytes_per_char=8):
    """
    Given a string 'text', return its blake2b hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -2581084514
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).intdigest(hex, bytes_per_char)
    return None


def string_to_hash_int(text, hex=True, bytes_per_char=8, bytes_per_int=4):
    """
    Given a string 'text', return its blake2b hash equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == -2581084514
    """
    if text:
        return blake2b(text.encode('utf-8'), digest_size=32).intdigest(hex, bytes_per_char, bytes_per_int)
    return None


def string_to_hash_int(text, hex=True, bytes_per_char=8, bytes_per_int=4, bytes_per_hex=2):
    """
    Given a string '