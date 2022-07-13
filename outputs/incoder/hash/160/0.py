
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if text == '':
        return None
    h = sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('sha1') == 'fa722c84448fb09fe6a02c5469a4