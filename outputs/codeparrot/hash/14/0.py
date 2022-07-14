def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    if not text:
        return None
    text = text.strip()
    if text.startswith('md5:'):
        text = text[5:]
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    :param filename: File to hash.
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

    :param filename: File to hash.
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

    :param env: Environment to hash.
    :returns: MD5 hex digest string.
    """
    return get_file_hash(env.get('CONTENT_LENGTH'), block_size=2 ** 20)


def get_env_file_hash(env):
    """
    Calculate the md5 hash for a file based on the environment.

    :param env: Environment to hash.
    :returns: MD5 hex digest string.
    """
    return get_file_hash(env.get('CONTENT_LENGTH'), block_size=2 ** 20