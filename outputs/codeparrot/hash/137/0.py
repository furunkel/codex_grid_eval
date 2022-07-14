def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    if len(text) == 40:
        text = text[0:40]
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    if len(filename) == 40:
        filename = filename[0:40]
    return hashlib.sha1(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('md5') == '99684e4a541d50b4ced1a9d65ad12dcb55f0925e0a568db5422e2d2af1fff7c3'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    if len(filename) == 40:
        filename = filename[0:40]
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('md5') == '99684e4a541d50b4ced1a9d65ad