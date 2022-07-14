def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    text = text.strip()
    if text.startswith('md5='):
        return hashlib.md5(text.split('md5=')[1]).hexdigest()
    return None


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :returns: The md5 hash of the file contents.
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
    Calculate a file contents for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :returns: The contents of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield data


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :returns: The md5 hash of the file contents.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield hashlib.md5(data).hexdigest()


def get_file_contents_as_string(filename, block_size=2 ** 20):
    """
    Calculate a file contents for a file.

    :param filename: Path to the file