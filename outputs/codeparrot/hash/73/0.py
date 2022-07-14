def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
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
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_contents(filename):
    """
    Return the contents of a file.

    :param filename: The filename to hash.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read()


def get_file_lines(filename):
    """
    Return the lines of a file.

    :param filename: The filename to hash.
    :return: The lines of the file.
    """
    with open(filename, 'rb') as f:
        return f.readlines()


def get_file_hash_from_file(filename):
    """
    Return the hash of a file.

    :param filename: The filename to hash.
    :return: The hash of the file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha384(f.read()).hexdigest()


def get_file_contents_as_string(filename):
    """
    Return the contents of a file as a string.

    :param filename: The filename to hash.
    :return: The contents of the file.
    """
    with open(filename, 'rb') as f:
        return f.read()


def get_file_hash