def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha3(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha3()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha3()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha3()
    with open(string, 'rb') as f:
        for block in iter(lambda: f.read(block