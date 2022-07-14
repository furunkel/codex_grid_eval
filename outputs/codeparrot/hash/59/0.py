def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha256(hashlib.sha256(text).digest()).hexdigest()


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
            hash_obj = hashlib.sha256()
            hash_obj.update(data)
            hash_obj.update(data)
            return hash_obj.hexdigest()


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
            hash_obj = hashlib.sha256()
            hash_obj.update(data)
            hash_obj.update(data)
            return hash_obj.hexdigest()


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
            if not data:
                break
           