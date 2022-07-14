def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '4b867b5ea469628e5e7f402651696d208e5c2fa0b4b9c628942a63f36b30c23afcda18c21aaf52e0fab1c6dfeac08f4ad5114dbb4bafd503f60380c4ed2dcf87'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The name of the file to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.md5(data).hexdigest()
            if hash_value == filename:
                return hash_value
            f.seek(0)


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: The name of the file to hash.
    :param block_size: The size of the blocks.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_value = hashlib.md5(data).hexdigest()
            if hash_value == filename:
                return hash_value
            f.seek(0)


def get_file_hash_from_string(string):
    """
    Calculate the hash of a file.

    :param string: The string to hash.
    :return: The hash of the file.
    """
    return get_file_hash(string, block_size=2 **