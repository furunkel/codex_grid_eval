def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if not text:
        return None
    return hashlib.sha384(text.encode('utf-8')).hexdigest()


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
            block_hash = hashlib.sha384(block).hexdigest()
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
            block_hash = hashlib.sha384(block).hexdigest()
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
            block =