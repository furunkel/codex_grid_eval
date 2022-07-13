
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a SHA3_512 hash string 'hash', return its string equivalent (e.g.
    '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de').
    If 'hash' is an empty string, return None.

    >>> hash_to_string('7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de') == 'md5'
    """
    if hash == '':
        return None
    return hash[:64]


def string_to_hexdigest(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent hex digest.
    If 'text' is an empty string, return None.

    >>> string_to_hexdigest('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hexdigest_to_string(hash):
    """
    Given a SHA3_512 hash hex digest 'hash', return its string equivalent (e.g.
    '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de').
    If 'hash' is an empty string, return None.

    >>> hexdigest_to_string('7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e