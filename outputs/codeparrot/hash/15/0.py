def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text is None:
        return None
    text = text.strip()
    if text == '':
        return None
    if len(text) == 40:
        return text
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file.

    :param filename: Path to a file.
    :param block_size: Block size to use when hashing.
    :return: The md5 hash of the file contents.
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

    :param filename: Path to a file.
    :param block_size: Block size to use when hashing.
    :return: The md5 hash of the file contents.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_file_hash_from_string(string, block_size=2 ** 20):
    """
    Calculate the md5 hash for a string.

    :param string: String to hash.
    :param block_size: Block size to use when hashing.
    :return: The md5 hash of the string contents.
    """
    return get_file_hash(string, block_size)


def get_file_hash_from_file_with_md5(filename, block_size=2 ** 20):
    """
    Calculate the md5 hash for a file with md5 hash.

    :param filename: Path to a file.
   