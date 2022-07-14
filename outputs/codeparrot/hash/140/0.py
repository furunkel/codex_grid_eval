def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read(block_size)).hexdigest()


def get_file_hash_from_string(string):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :return: The hash of the file.
    """
    return get_file_hash(string, block_size=2 ** 20)


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read(block_size)).hexdigest()


def get_file_hash_from_file_with_sha1(