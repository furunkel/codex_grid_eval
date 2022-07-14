def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha224()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_or_block_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file, or block hash.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file or block hash.
    """
    hash_ = hashlib.sha224()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_or_block_hash_or_none(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file, or block hash.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file or block hash.
    """
    hash_ = hashlib.sha224()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_or_none(filename,