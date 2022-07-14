def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash for the file.
    :returns: The hex digest of the MD5 hash of the file contents.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(open(filename, 'rb').read()).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_file_contents(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file contents for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash for the file.
    :returns: The hex digest of the MD5 hash of the file contents.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(open(filename, 'rb').read()).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_file_lines(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file contents for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when hashing.
    :param md5: Optional MD5 hash for the file.
    :returns: The hex digest of the MD5 hash of the file contents.
    """
    if not filename:
        return None
    if md5:
       