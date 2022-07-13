
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if text == '':
        return None
    return blake2b_hash(text)


def blake2b_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b(text, digest_size=32)


def blake2b_hmac(key, text):
    """
    Given a BLAKE2B key 'key' and a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hmac('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b_hash(HMAC(key, text, digest_size=32))


def blake2b_hmac_digest(key, text):
    """
    Given a BLAKE2B key 'key' and a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> blake2b_hmac_digest('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    return blake2b_hash(HMAC(key, text, digest_size=32, digestmod=hashlib.sha256))


def blake2b_hmac_digest_from_file(key, filename):
    """
    Given a BLAKE2B key 'key' and a file 'filename', return its BLAKE2B hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> blake2b_hmac_digest_from_file('0', '0') == 'e9f11462495