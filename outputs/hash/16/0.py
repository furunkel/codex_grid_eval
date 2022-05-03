
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA512 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha512(hash.encode('utf-8')).hexdigest()


def hash_to_hex(hash):
    """
    Given a SHA512 hash 'hash', return its hexadecimal equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_hex('b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47') == '0x48656c6c6f20776f726c64'
    """
    if hash == '':
        return None
    else:
        return hex(int(hash, 16))


def hex_to_hash(hex):
    """
    Given a hexadecimal 'hex', return its SHA512 hash equivalent.
    If 'hex' is an empty string, return None.

    >>> hex_to_hash('0x48656c6c6f20776f726c64') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600