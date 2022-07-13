
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
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
    Given a sha3_512 hash string 'hash', return its string equivalent string.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de') == 'md5'
    """
    if hash == '':
        return None
    return hash[:32].decode('utf-8')


def hash_of_string(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> hash_of_string('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if text == '':
        return None
    h = hashlib.sha3_512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file('README.md') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """
    if filename == '':
        return None
    with open(filename, 'rb') as f:
        h = hashlib.sha3_512()
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def hash_of_file_or_string(filename, text):
    """
    Given a filename 'filename' and a string 'text', return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> hash_of_file_or_string('README.md', 'md5') == '7e82fff92f72d30033578cf1a2d3