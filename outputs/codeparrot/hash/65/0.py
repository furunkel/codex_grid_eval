def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if not text:
        return None
    return hashlib.sha256(hashlib.sha256(text.encode('utf-8')).digest()).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read(block_size)).hexdigest()


def get_file_contents(filename, block_size=2 ** 20):
    """
    Calculate the contents of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read(block_size)


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read(block_size)).hexdigest()


def get_file_contents_as_string(filename, block_size=2 ** 20):
    """
    Calculate the contents of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read(block_size)


def get_file_hash_from_file_contents(filename, block_size=2