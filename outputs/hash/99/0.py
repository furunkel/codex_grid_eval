
def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA512 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99') == '0'
    """
    if hash == '':
        return None
    return hashlib.sha512(bytes.fromhex(hash)).hexdigest()


def hash_to_int(hash):
    """
    Given a SHA512 hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99') == 0
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its SHA512 hash equivalent string.
    If 'integer' is 0, return None.

    >>> int_to_hash(0) == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if integer == 0:
        return None
    return hashlib.sha512(integer.