def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return hashlib.sha384(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha384 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha384(filename.encode('utf-8')).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.md5(filename.encode('utf-8')).hexdigest()


def get_file_size_in_bytes(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return os.path.getsize(filename)


def get_file_md5_from_hash(hash):
    """
    Given a hash, return its md5 equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash is None:
        return None
    return hashlib.md5(hash.encode('utf-8')).hexdigest()


def get_file_size_in_bytes_and_md5(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return os.path.getsize(filename) + get_file_size_in_bytes(filename)


def get_file_md5_from_hash_and_size(hash, size):
    """
    Given a hash, return its md5 equivalent string.
    If 'hash