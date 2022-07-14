def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c'
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
        for block in iter(lambda: f.read(block_size), b''):
            block = block.decode('utf-8')
            block_hash = hashlib.sha256(block).hexdigest()
            if block_hash == block:
                return block_hash
    return None


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            block = block.decode('utf-8')
            block_hash = hashlib.sha256(block).hexdigest()
            if block_hash == block:
                return block_hash
    return None


def get_file_hash_from_string(string):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :return: The hash of the file.
    """
    with open(string, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

   