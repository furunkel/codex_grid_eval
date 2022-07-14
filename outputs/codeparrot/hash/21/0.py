def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha1 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha1(filename).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
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

    >>> get_file_lines('0') == ['b6589fc6ab0dc82cf12099d1c2d40ab994e8410c']
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).readlines()


def get_file_lines_with_encoding(filename, encoding):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines_