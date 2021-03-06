def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    return hashlib.sha512(filename.encode('utf-8')).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    with open(filename, 'r') as f:
        return f.read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    with open(filename, 'r') as f:
        return f.readlines()


def get_file_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    with open(filename, 'r') as f:
        return f.readlines()


def get_file_lines_with_hashes_and_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    with open(filename, 'r') as f:
        return f.readlines()


def get_file_lines_with_hashes_and_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if filename is None:
        return None
    with open(filename, 'r') as f:
        return f.readlines()


def get_file_lines_