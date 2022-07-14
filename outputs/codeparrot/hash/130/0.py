def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    if len(text) == 40:
        return text
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read(block_size)).hexdigest()


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
        return hashlib.sha1(f.read(block_size)).hexdigest()


def get_file_contents_as_string(filename, block_size=2 ** 20):
    """
    Calculate the contents of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read(block_size)