
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return base64.b64encode(h.digest()).decode('utf-8')


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return base64.b64encode(h.digest()).decode('utf-8')


def string_to_hash_base64_utf8(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent base64 utf8 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8('md5