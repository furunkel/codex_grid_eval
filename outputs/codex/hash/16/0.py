
def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_hash_sha1(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha1('sha1') == 'f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_hash_sha256(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha256('sha256') == 'f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('sha512') == 'f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7e9b8f9e9b8f8c7