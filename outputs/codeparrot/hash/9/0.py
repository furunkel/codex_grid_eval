def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if not text:
        return None
    text = text.strip()
    if len(text) == 0:
        return None
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :return: MD5 hash string.
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the MD5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :return: MD5 hash string.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_hash_from_env(env):
    """
    Calculate the MD5 hash for a file.

    :param env: Environment to use when reading.
    :return: MD5 hash string.
    """
    return get_file_hash_from_file(env.get('PATH', ''), block_size=2 ** 20)


def get_env_file():
    """
    Return the path to the file that contains the file that contains
    the file that contains the file that contains the file that contains
    the file that contains the file that contains the file that contains
    the file that contains the file that contains the file that contains
    the file that contains the file that contains the file that contains the file
    that contains the file that