def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha224(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            block = block.decode('utf-8')
            block_hash = hashlib.sha224(block).hexdigest()
            if block_hash == block:
                return block_hash
    return None


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            block = block.decode('utf-8')
            block_hash = hashlib.sha224(block).hexdigest()
            if block_hash == block:
                return block_hash
    return None


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(string, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            block = block.decode('utf-8')
            block