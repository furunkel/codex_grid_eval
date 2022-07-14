def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
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
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.sha224(data).hexdigest()
            if not hash_value in BLOCK_HASHES:
                return None
            BLOCK_HASHES[hash_value] = hash_value
    return BLOCK_HASHES[filename]


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.sha224(data).hexdigest()
            if not hash_value in BLOCK_HASHES:
                return None
            BLOCK_HASHES[hash_value] = hash_value
    return BLOCK_HASHES[filename]


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(string, 'rb') as f:
        while True:
            data = f.read(block_size)
           