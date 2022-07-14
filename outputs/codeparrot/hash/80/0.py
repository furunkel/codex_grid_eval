def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha384(text).hexdigest()


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
            hash_value = hashlib.sha384(data).hexdigest()
            if not hash_value in BLOCK_HASHES:
                break
            BLOCK_HASHES[hash_value] = hash_value
    return BLOCK_HASHES[filename]


def get_file_hash_or_block_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file or block.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file or block.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.sha384(data).hexdigest()
            if hash_value in BLOCK_HASHES:
                return BLOCK_HASHES[hash_value]
    return None


def get_file_hash_or_block_hash_or_none(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file or block.

    :param filename: The filename to hash.
    :param block_size: The size