def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha512(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha512(f.read(block_size)).hexdigest()


def get_file_contents(filename, block_size=2 ** 20):
    """
    Calculate the contents of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read(block_size)


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha512(f.read(block_size)).hexdigest()


def get_file_contents_as_string(filename, block_size=2 ** 20):
    """
    Calculate the contents of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The contents of the file.
    """
    with