def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-224 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if not filename:
        return None
    return hashlib.sha224(filename.encode('utf-8')).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if not filename:
        return None
    return hashlib.md5(filename.encode('utf-8')).hexdigest()


def get_file_sha1(filename):
    """
    Given a filename, return its sha-1 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_sha1('Hallo welt') == 'fa