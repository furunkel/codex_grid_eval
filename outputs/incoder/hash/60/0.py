
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(filename):
    """
    Given a filename 'filename', return its SHA256 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()


def hash_of_file_or_string(file_or_string):
    """
    Given a file object 'file_or_string', return its SHA256 hash equivalent string.
    If 'file_or_string' is an empty string, return None.
    """
    if file_or_string is None:
        return None
    h = hashlib.sha256()
    if isinstance(file_or_string, str):
        file_or_string = StringIO(file_or_string)
    for chunk in iter(lambda: file_or_string.read(4096), b''):
        h.update(chunk)
    return h.hexdigest()


def hash_of_file_or_string_or_none(file_or_string):
    """
    Given a file object 'file_or_string', return its SHA256 hash equivalent string.
    If 'file_or_string' is an empty string, return None.
    """
    if file_or_string is None:
        return None
    h = hashlib.sha256()
    if isinstance(file_or_string, str):
        file_or_string = StringIO(file_or_string)
    for chunk in iter(lambda: file_or_string.read(4096), b''):
        h.update(chunk)
    return h.hexdigest()


def hash_of_file_or_string_or_none(file_or_string):
    """
    Given a file object 'file_or_string', return its SHA256 hash equivalent string.
    If 'file_or_string' is an empty string, return None.
    """
    if file_or_string is None:
        return None
    h = hashlib.sha256()
    if isinstance(file_or_string, str):
        file_or_string = StringIO(file_or_string)
    for chunk in iter(lambda: file_or_string.read(4096), b''):
        h.update(chunk)
    return h.hexdigest()


def hash_of_file_or_string_or_none_or_empty(file_or_string):
    """
    Given a file object 'file_or_string', return its SHA256 hash equivalent string.
    If 'file_or_string' is an empty string, return None.
    """
    if file_or_string is None:
