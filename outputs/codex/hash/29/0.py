
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA1 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('c1ea94f7e524679d0cf34ab7b0b28abe41ba732b') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha1(hash).hexdigest()


def hash_to_hex(hash):
    """
    Given a SHA1 hash 'hash', return its hexadecimal equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_hex('c1ea94f7e524679d0cf34ab7b0b28abe41ba732b') == '0x6d6435'
    """
    if hash == '':
        return None
    else:
        return hex(int(hash, 16))


def hex_to_hash(hex):
    """
    Given a hexadecimal 'hex', return its SHA1 hash equivalent.
    If 'hex' is an empty string, return None.

    >>> hex_to_hash('0x6d6435') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if hex == '':
        return None
    else:
        return hashlib.sha1(hex).hexdigest()


def hex_to_string(hex):
    """
    Given a hexadecimal 'hex', return its string equivalent.
    If 'hex' is an empty string, return None.

    >>> hex_to_string('0x6d6435') == 'md5'
    """
    if hex == '':
        return None
    else:
        return hashlib.sha1(hex).hexdigest()


def string_to_hex(text):
    """
    Given a string 'text', return its hexade