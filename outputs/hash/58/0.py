
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') == 'sha1'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') == 156582
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def int_to_hash(integer):
    """
    Given an integer 'integer', return its hash equivalent.
    If 'integer' is an empty string, return None.

    >>> int_to_hash(156582) == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if integer == '':
        return None
    else:
        return hex(integer)[2:]


def hash_to_base64(hash):
    """
    Given a hash 'hash', return its base64 equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_base64('b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f') ==