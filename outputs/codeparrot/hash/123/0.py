def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha1(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return os.path.getsize(filename)
    return None


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If