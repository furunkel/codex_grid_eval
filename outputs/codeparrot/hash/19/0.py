def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
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

    >>> get_file_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
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

    >>> get_file_contents('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
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

    >>> get_file_lines('Hello world') == ['7b502c3a1f48c8609ae212cdfb639dee39673f5e']
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).readlines()


def get_file_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines_with_