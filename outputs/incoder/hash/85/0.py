
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return 