def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if not text:
        return None
    text = text.strip()
    if text.startswith('sha1='):
        text = text[len('sha1='):]
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :returns: MD5 hex digest string.
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
    Calculate the md5 hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when reading.
    :returns: MD5 hex digest string.
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
    Calculate the md5 hash for a file based on the environment.

    :param env: The environment to use when looking up the file.
    :returns: MD5 hex digest string.
    """
    return get_file_hash(env.get('PATH_INFO'), block_size=2 ** 20)


def get_env_file_hash(env_file):
    """
    Calculate the md5 hash for a file based on the environment.

    :param env_file: The path to the file.
    :returns: MD5 hex digest string.
    """
    return get_file_hash(env