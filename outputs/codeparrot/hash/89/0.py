def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
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
            hash_value = hashlib.sha384(data).hexdigest()
            if not hash_value in hashes:
                hashes[hash_value] = []
            hashes[hash_value].append(data)
    return hashes


def get_file_hashes_for_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of each block.
    :return: The hash of the file.
    """
    hashes = {}
    with open(filename, 'rb') as f:
       