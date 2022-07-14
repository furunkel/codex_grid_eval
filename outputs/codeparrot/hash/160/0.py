def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if not text:
        return None
    return hashlib.sha3(text.encode('utf-8')).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha3(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha3(f.read(block_size)).hexdigest()


def get_file_hash_from_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: The url to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    return get_file_hash_from_file(url, block_size)


def get_file_hash_from_file_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: The url to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    return get_file_