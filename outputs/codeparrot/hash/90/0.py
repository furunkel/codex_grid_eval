def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return hashlib.sha512(filename.encode('utf-8')).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return hashlib.md5(filename.encode('utf-8')).hexdigest()


def get_file_size_in_bytes(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5_from_hash(hash):
    """
    Given a hash, return its md5 equivalent string.
    If 'hash' is an empty string, return None.
    """
    if not hash:
        return None
    return hashlib.md5(hash.encode('utf-8')).hexdigest()


def get_file_size_in_bytes_and_md5(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.getsize(filename)


def get_file_md5_from_hash_and_size(hash, size):
    """
    Given a hash, return its md5 equivalent string.
    If 'hash' is an empty string, return None.
    """
    if not hash:
        return None
   