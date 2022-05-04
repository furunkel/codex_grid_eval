
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if text == '':
        return None
    return blake2b(text.encode('utf-8'), digest_size=64).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2B hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == '0'
    """
    if hash == '':
        return None
    return blake2b(bytes.fromhex(hash), digest_size=1).hexdigest()


def hash_to_int(hash):
    """
    Given a BLAKE2B hash 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == 0
    """
    if hash == '':
        return None
    return int(hash_to_string(hash))


def int_to_hash(integer):
    """
    Given an integer 'integer', return its BLAKE2B hash equivalent string.
    If 'integer' is 0, return None.

    >>> int_to_hash(0) == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'