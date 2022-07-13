
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    return hashlib.sha1(text).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == '0'
    """
    if hash == '':
        return None
    return hashlib.sha1(hash).hexdigest()


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == 0
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its hash equivalent.
    If 'integer' is an empty string, return None.

    >>> int_to_hash(0) == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if integer == '':
        return None
    return hashlib.sha1(str(integer)).hexdigest()


def hash_to_hex(hash):
    """
    Given a hash 'hash', return its hexadecimal equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_hex('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == '0x0'
    """
    if hash == '':
        return None
    return hex(int(hash, 16))


def hex_to_hash(hexadecimal):
    """
    Given a hexadecimal 'hexadecimal', return its hash equivalent.
    If 'hexadecimal' is an empty string, return None.

    >>> hex_to