def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha224(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-224 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha224(filename).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).readlines()


def get_file_lines_with_n_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).readlines()


def get_file_lines_with_n_lines_and_n_bytes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).readlines()


def get_file_lines_with_n_lines_and_n_bytes_and_n_lines(filename