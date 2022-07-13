
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if text == '':
        return None
    return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.

    >>> hash_to_string('cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e') == 'sha1'
    """
    if hash is None:
        return ''
    return hash


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is None, return 0.

    >>> hash_to_int('cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e') == 0xcd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e
    """
    if hash is None:
        return 0
    return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its hash equivalent.
    If 'integer' is 0, return None.

    >>> int_to_hash(0xcd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e) == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if integer == 0:
        return None
    return '{:064x}'.format(integer)


def hash_to_hex(hash):
    """
    Given a hash 'hash', return its hexadecimal equivalent.
   