def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
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

    >>> get_file_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
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

    >>> get_file_size('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
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

    >>> get_file_md5('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.md5(filename).hexdigest()


def get_file_sha1(filename):
    """
    Given a filename, return its sha-1 hash equivalent string.
    If 'filename' is an empty