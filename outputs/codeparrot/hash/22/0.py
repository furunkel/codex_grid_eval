def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if not text:
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha1 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if not filename:
        return None
    return hashlib.sha1(filename.encode('utf-8')).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if not filename:
        return None
    with open(filename, 'r') as f:
        return f.read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines('sha1') == ['415ab40ae9b7cc4e66d6769cb2c08106e8293b48']
    """
    if not filename:
        return None
    with open(filename, 'r') as f:
        return f.readlines()


def get_file_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines_with_hashes('sha1') == ['415ab40ae9b7cc4e66d6769cb2c08106e8293b48']
    """
    if not filename:
       