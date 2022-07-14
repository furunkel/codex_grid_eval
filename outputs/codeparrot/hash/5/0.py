def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :return: MD5 hex digest string.
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :return: MD5 hex digest string.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the md5 hash for a string.

    :param string: String to hash.
    :param block_size: Block size to use when reading.
    :return: MD5 hex digest string.
    """
    return get_file_hash(string, block_size)


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file with md5.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :return: MD5