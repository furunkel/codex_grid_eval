def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA1 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('hello.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return hashlib.sha1(filename).hexdigest()


def get_file_path(filename):
    """
    Given a filename, return its SHA1 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_path('hello.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return hashlib.sha1(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('hello.txt') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if not filename:
        return None
    filename = filename.strip()
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('hello.txt') == '7b502c3a1f48