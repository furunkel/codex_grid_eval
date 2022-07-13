
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.
    """

def get_file_hash(filename):
    """
    Given a filename, return its sha-384 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha384(open(filename, 'rb').read()).hexdigest()

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
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def get_file_size_and_md5(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None, None
    return os.path.getsize(filename), hashlib.md5(open(filename, 'rb').read()).hexdigest()

def get_file_md5_and_size(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None, None
    return os.path.getsize(filename), hashlib.md5(open(filename, 'rb').read()).hexdigest()

def get_file_size_and_md5_and_size(filename):
    """
    Given a filename, return its size and md5 equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None, None
    return os.path.getsize(filename), hashlib.md5(open(filename, 'rb').read()).hexdigest(), hashlib.md5(open(filename, 'rb').read()).hexdigest()

