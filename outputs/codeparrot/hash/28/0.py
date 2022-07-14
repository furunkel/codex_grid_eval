def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '415ab40ae9b7cc4e66d6769cb2c08106e8293b48'
    """
    if not text:
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_file_hash(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash to be used.
    :returns: The hex digest of the file.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()


def get_file_contents(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file contents for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash to be used.
    :returns: The hex digest of the file.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return f.read()


def get_file_lines(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file lines for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash to be used.
    :returns: The hex digest of the file.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(filename.encode('utf-8')).hexdigest()
    else:
        with open(filename, 'rb') as f