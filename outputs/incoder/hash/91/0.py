
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not text:
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not text:
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha512_hexdigest(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not text:
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_sha512_hexdigest_bytes(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest_bytes('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not text:
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest().encode('utf-8')


def string_to_hash_sha512_hexdigest_bytes_hex(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_sha512_hexdigest_bytes_hex('Hello world') == 'b