
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if text == '':
        return None
    return blake2b_hash(text)


def blake2b_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b(text, digest_size=32)


def blake2b_salted_hash(text, salt):
    """
    Given a string 'text' and a salt 'salt', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_hash('0', '0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b(text + salt, digest_size=32)


def blake2b_salted_hash_with_prefix(text, salt, prefix):
    """
    Given a string 'text' and a salt 'salt' and a prefix 'prefix', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_hash_with_prefix('0', '0', '0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b(prefix + text + salt, digest_size=32)


def blake2b_salted_hash_with_prefix_and_salt(text, salt, prefix, salt):
    """
    Given a string 'text' and a salt 'salt' and a prefix 'prefix' and another salt 'salt', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_salted_