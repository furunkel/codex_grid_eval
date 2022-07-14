def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    if not text:
        return None
    text = text.strip()
    if text == '':
        return None
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :returns: MD5 hash of file contents.
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_contents(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :returns: MD5 hash of file contents.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :returns: MD5 hash of file contents.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_hash_from_file_contents(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file