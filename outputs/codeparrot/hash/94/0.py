def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '4af46fa0152c825afee230022f46e3aedb0a9ee2a3dc20e30821a4d263327074b26455f29578812876011dd921132c6ed813b38d16b1b2a1c1fa7cea1a6b1fd9'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha512(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha512(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha512(f.read(block_size)).hexdigest()


def get_file_hash_from_string(string):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :return: The hash of the file.
    """
    return get_file_hash(string_to_hash(string))


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib