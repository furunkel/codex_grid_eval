def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
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

    >>> get_file_contents('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return open(filename).read()


def get_file_contents_as_string(filename):
    """