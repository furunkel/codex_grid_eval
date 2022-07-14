def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
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
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield data


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The filename to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield data


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(string, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            yield data


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """