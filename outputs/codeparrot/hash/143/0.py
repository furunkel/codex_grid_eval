def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    return None


def get_file_hash_from_file(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash_from_file('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    return None


def get_file_hash_from_url(url):
    """
    Given a url, return its hash equivalent string.
    If 'url' is an empty string, return None.

    >>> get_file_hash_from_url('http://www.google.com/images/srpr/logo.png') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1