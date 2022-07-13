
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a sha224 hash string, return its string equivalent hash.
    If 'hash' is an empty string, return None.
    """
    if hash is None:
        return None
    h = hashlib.sha224()
    h.update(hash.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path):
    """
    Given a path to a file, return its sha224 hash equivalent string.
    If 'path' is an empty string, return None.
    """
    if path is None:
        return None
    h = hashlib.sha224()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_of_string(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path, block_size=4096):
    """
    Given a path to a file, return its sha224 hash equivalent string.
    If 'path' is an empty string, return None.
    """
    if path is None:
        return None
    h = hashlib.sha224()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_of_string(text, block_size=4096):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path, block_size=4096):
    """
    Given a path to a file, return its sha224 hash equivalent string.
    If 'path' is an empty string, return None.
    """
    if path is None:
        return None
    h = hashlib.sha224()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_of_string(text, block_size=4096):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_of_file(path, block_size=4096):
    """
    Given a path to 