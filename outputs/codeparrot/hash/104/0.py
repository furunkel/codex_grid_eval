def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if not text:
        return None
    if len(text) == 40:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its sha-512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if not filename:
        return None
    if len(filename) == 40:
        return hashlib.sha512(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if not filename:
        return None
    if len(filename) == 40:
        return os.path.getsize(filename)
    return None


def get_file