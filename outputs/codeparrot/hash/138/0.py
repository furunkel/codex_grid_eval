
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """

def get_hash(text):
    """
    Given a string 'text', return its hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return hashlib.sha256(hashlib.sha256(text.encode('utf-8')).digest()).hexdigest()

def get_hash_from_file(filename):
    """
    Given a file name, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha256(open(filename, 'rb').read()).hexdigest()

def get_hash_from_string(string):
    """
    Given a string 'string', return its hash equivalent string.
    If 'string' is an empty string, return None.
    """
    if string is None:
        return None
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def get_hash_from_file_with_md5(filename):
    """
    Given a file name, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha256(open(filename, 'rb').read()).hexdigest()

def get_hash_from_file_with_sha1(filename):
    """
    Given a file name, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha1(open(filename, 'rb').read()).hexdigest()

def get_hash_from_file_with_sha224(filename):
    """
    Given a file name, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha224(open(filename, 'rb').read()).hexdigest()

def get_hash_from_file_with_sha256(filename):
    """
    Given a file name, return its hash equivalent string.
    If '