
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_string_2(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_2('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_string_3(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_3('3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_string_4(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string_4('3ebff31b62c0637c