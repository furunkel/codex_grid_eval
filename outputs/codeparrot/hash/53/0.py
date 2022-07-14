def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-224 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return hashlib.sha224(filename.encode('utf-8')).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return hashlib.md5(filename.encode('