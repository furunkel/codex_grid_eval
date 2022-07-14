def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return hashlib.sha256(filename.encode('utf-8')).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return hashlib.md5(filename.encode('utf-8')).hexdigest()


def get_file_