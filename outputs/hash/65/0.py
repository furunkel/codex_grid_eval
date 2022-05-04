
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA256 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA256 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd') == 1023456789
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA256 hash equivalent string.
    If 'integer' is an empty string, return None.

    >>> int_to_hash(1023456789) == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if integer == '':
        return None
    else:
        return hashlib.sha256(str(integer).encode('utf-8')).hexdigest()


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent.
    If 'text' is an empty string, return None.

    >>> string_to_int('md5') == 1023456789
    """
    if text == '':
        return None