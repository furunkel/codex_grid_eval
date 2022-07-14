def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha256(hashlib.sha256(text).digest()).digest()


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
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
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
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return f.read(block_size)


def get_file_hash_