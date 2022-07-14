def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha3(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha3(filename).hexdigest()


def get_file_hash_from_file(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash_from_file('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename