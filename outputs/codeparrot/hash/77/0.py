def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
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
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_hash_from_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: The url to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with urllib.request.urlopen(url) as f:
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_hash_from_file_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: The url to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with urllib.request.urlopen(url) as f:
        return hashlib.sha384(