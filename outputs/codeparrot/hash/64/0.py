def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha256(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha256(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('