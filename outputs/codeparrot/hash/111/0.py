def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate a file hash for a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            return hashlib.sha1(data).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate a file hash for a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            return hashlib.sha1(data).hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate a file hash for a string.

    :param string: The string to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    return get_file_hash_from_string(string, block_size)


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate