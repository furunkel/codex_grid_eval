def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha1()
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

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha1()
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

    :param string: The string to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hash_ = hashlib.sha1()
    with open(string, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_.update(data)
    return hash_.hexdigest()


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate