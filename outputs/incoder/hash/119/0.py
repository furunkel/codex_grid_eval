
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=32)


def hash_to_string(hash):
    """
    Given a BLAKE2B hash string, return its string equivalent if possible.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87') == 'md5'
    """
    if hash is None:
        return None
    return hash[:16].decode('hex')


def blake2b_to_hex(blake2b):
    """
    Given a BLAKE2B hash string, return its hex equivalent if possible.
    If 'hash' is an empty string, return None.

    >>> blake2b_to_hex('4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87') == '5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if blake2b is None:
        return None
    return blake2b[:32].encode('hex')


def hex_to_blake2b(hex):
    """
    Given a hex string, return its BLAKE2B hash equivalent if possible.
    If 'hash' is an empty string, return None.

    >>> hex_to_blake2b('5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf