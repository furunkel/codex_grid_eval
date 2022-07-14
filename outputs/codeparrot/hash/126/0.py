def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return os.path.getsize(filename)
    return None


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size_and_md5(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None, None
    if isinstance(filename, str):
        return os.path.getsize(filename), hashlib.md5(filename.encode('utf-8')).hexdigest()
    return None, None


def get_file_md5_and_size(filename):
    """
    Given a filename, return its md5 and size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None, None
    if isinstance(filename, str):
        return os.path.getsize(filename), os.path.getsize(filename)
    return None, None


def get_file_md5_and_md5_and_size(filename):
    """
    Given a filename, return