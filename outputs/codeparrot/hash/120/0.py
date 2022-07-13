
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """

def get_hash_from_text(text):
    """
    Given a string 'text', return its hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return hashlib.sha256(hashlib.sha256(text.encode('utf-8')).digest()).digest()

def get_hash_from_file(filename):
    """
    Given a filename 'filename', return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha256(open(filename, 'rb').read()).digest()

def get_hash_from_lines(lines):
    """
    Given a list of lines, return its hash equivalent string.
    If 'lines' is an empty list, return None.
    """
    if lines is None:
        return None
    return hashlib.sha256(lines).digest()

def get_hash_from_file_lines(filename, lines):
    """
    Given a list of lines, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha256(open(filename, 'rb').read()).digest()

def get_hash_from_lines_with_hashes(lines, hashes):
    """
    Given a list of lines, return its hash equivalent string.
    If 'lines' is an empty list, return None.
    """
    if lines is None:
        return None
    return hashlib.sha256(lines).digest()

def get_hash_from_file_hashes(filename, hashes):
    """
    Given a list of hashes, return its hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha256(open(filename, 'rb').read()).digest()

def get_hash_from_file_hashes_with_hashes(filename, hashes):
    """
    Given a list of hashes, return its hash equivalent string.
    If 'filename'