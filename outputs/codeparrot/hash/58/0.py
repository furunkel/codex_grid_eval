def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not text:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha256 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not filename:
        return None
    return hashlib.sha256(filename.encode('utf-8')).hexdigest()


def get_file_contents(filename):
    """
    Given a filename, return its contents as a string.
    If 'filename' is an empty string, return None.

    >>> get_file_contents('sha1') == 'b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f'
    """
    if not filename:
        return None
    return open(filename).read()


def get_file_lines(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines('sha1') == ['b1565820a5cdac40e0520d23f9d0b1497f240ddc51d72eac6423d97d952d444f']
    """
    if not filename:
        return None
    return open(filename).readlines()


def get_file_lines_with_hashes(filename):
    """
    Given a filename, return its lines as a list of strings.
    If 'filename' is an empty string, return None.

    >>> get_file_lines_with_