def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
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
    with open(filename, 'rb') as f:
        return hashlib.sha224(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha224(f.read(block_size)).hexdigest()


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
    return get_file_hash_from_file(url, block_size)


def get_file_hash_from_url_with_md5(url, block_size=2 ** 20):
    """
    Calculate the hash of a file