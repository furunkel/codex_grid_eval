def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    return hashlib.sha384(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-384 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return hashlib.sha384(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return hashlib.md5(filename).hexdigest()


def get_file_sha1(filename):
    """
    Given a filename, return its sha-1 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return hashlib.sha1(filename).hexdigest()


def get_file_size_and_md5(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0:
        return None
    return os.path.getsize(filename), hashlib.md5(filename).hexdigest()


def get_file_md5_and_sha1(filename):
    """
    Given a filename, return its md5 and sha-1 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if len(filename) == 0