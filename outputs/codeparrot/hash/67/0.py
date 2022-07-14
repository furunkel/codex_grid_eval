def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()
    return None


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
            hash_value = hashlib.sha256(data).hexdigest()
            if not hash_value in file_hashes:
                file_hashes[hash_value] = []
            file_hashes[hash_value].append(data)
    return file_hashes


def get_file_hashes(filename):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :return: The hash of the file.
    """
    hashes = {}
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.sha256(data).hexdigest()
            if not hash_value in hashes:
                hashes[hash_value] = []
            hashes[hash_value].append(data)
    return hashes


def get_file_hashes_for_file(file_path, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param file_path: The path to the file.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hashes = {}
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block