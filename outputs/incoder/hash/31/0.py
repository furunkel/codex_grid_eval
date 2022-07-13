
def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_digest(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).digest()


def string_to_hash_digest64(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest64('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).digest()


def string_to_hash_digest256(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest256('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).digest()


def string_to_hash_digest512(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest512('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).digest()


def string_to_hash_digest512_hex(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest512_hex('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_digest256_hex(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_digest256_hex('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


