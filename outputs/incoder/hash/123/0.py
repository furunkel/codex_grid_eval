
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if text == '':
        return None
    h = blake2b(digest_size=32, salt=b'', person=b'', key=b'', digest_type=blake2b.SHA1)
    h.update(text.encode())
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a blake2b hash string, return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == '0'
    """
    if hash == '':
        return None
    h = blake2b(digest_size=32, salt=b'', person=b'', key=b'', digest_type=blake2b.SHA1)
    h.update(hash.encode())
    return h.digest()


def hash_to_int(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == 0
    """
    if hash == '':
        return None
    h = blake2b(digest_size=32, salt=b'', person=b'', key=b'', digest_type=blake2b.SHA1)
    h.update(hash.encode())
    return int(h.hexdigest(), 16)


def int_to_hash(int_hash):
    """
    Given an integer hash, return its blake2b hash equivalent string.
    If 'int_hash' is an empty string, return None.

    >>> int_to_hash(0) == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if int_hash == 0:
        return None
    h = blake2b(digest_size=32, salt=b'', person=b'', key=b'', digest_type=bla