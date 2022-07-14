def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'fa722c84448fb09fe6a02c5469a4af7a2e2d829b904c126b6264ff675ff1f35db25d4d0ddcdeb101eaf0114a68e75fd11e2ca2b45ebfbc0d91e6172a6a198f65'
    """
    if not text:
        return None
    text = to_unicode(text)
    if len(text) == 40:
        return hashlib.sha3_512(text).hexdigest()
    return None


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: path to the file
    :param block_size: the size of each block
    :return: the hash
    """
    hash_ = hashlib.sha1()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_or_block_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: path to the file
    :param block_size: the size of each block
    :return: the hash
    """
    hash_ = hashlib.sha1()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_.update(block)
    return hash_.hexdigest()


def get_file_hash_or_block_hash_or_none(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file or None.

    :param filename: path to the file
    :param block_size: the size of each block
    :return: the hash
    """
    hash_ = hashlib.sha1()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size),