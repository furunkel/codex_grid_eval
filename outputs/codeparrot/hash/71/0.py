def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha256(hashlib.sha256(text).digest()).digest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: String to hash.
    :param block_size: Block size to use when hashing.
    :return: Hash of the file.
    """
    hash_ = hashlib.sha256()
    with open(string, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_from_file_with_md