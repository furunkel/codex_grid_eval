def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its sha-1 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    if isinstance(filename, str):
        return os.path.getsize(filename)
    return None


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    if isinstance(filename, str):
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    return None


def get_file_sha1(filename):
    """
    Given a filename, return its sha-1 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size_and_md5(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None, None
    if isinstance(filename, str):
        return os.path.getsize(filename), None
    return None, None


def get_file_md5_and_sha1(filename):
    """
    Given a filename, return its md5 and sha-1 hash equivalent string.
    If 'filename' is an empty string