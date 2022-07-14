def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha224(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha224()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_.update(data)
    return hash_.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha224()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_.update(data)
    return hash_.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: String to hash.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha224()
    with open(string, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_.update(data)
    return hash_.hexdigest()


def get_file_hash_from_file_with_md5(filename