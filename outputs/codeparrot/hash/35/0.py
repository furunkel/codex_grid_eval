def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-1 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha1(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.md5(filename).hexdigest()


def get_file_size_md5(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_