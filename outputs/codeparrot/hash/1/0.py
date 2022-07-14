def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    text = text.strip()
    if text.startswith('md5='):
        text = text[len('md5='):]
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when reading.
    :param md5: Optional MD5 hash to be used.
    :returns: The md5 hash of the file contents.
    """
    if not filename:
        return None
    if not md5:
        md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_file_contents(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file contents for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when reading.
    :param md5: Optional MD5 hash to be used.
    :returns: The contents of the file.
    """
    if not filename:
        return None
    if not md5:
        md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_hash_from_file(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a hash for a file.

    :param filename: Path to file.
    :param block_size: Block size to use when reading.
    :param md5: Optional MD5 hash to be used.
    :returns: The hash of the file contents