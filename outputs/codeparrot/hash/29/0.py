def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if not text:
        return None
    text = text.strip()
    if text == '':
        return None
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: File to hash.
    :param block_size: Block size to use.
    :return: Hash of file.
    """
    hash_obj = hashlib.sha1()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_obj.update(block)
    return hash_obj.hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: File to hash.
    :param block_size: Block size to use.
    :return: Hash of file.
    """
    hash_obj = hashlib.sha1()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hash_obj.update(block)
    return hash_obj.hexdigest()


def get_file_hash_from_string(string):
    """
    Calculate the hash of a file.

    :param string: File to hash.
    :return: Hash of file.
    """
    hash_obj = hashlib.sha1()
    with open(string, 'rb') as f:
        for block in iter(lambda: f.read(block), b''):
            hash_obj.update(block)
    return hash_obj.hexdigest()


def get_file_hash_from_file_obj(file_obj):
    """
    Calculate the hash of a file.

    :param file_obj: File to hash.
    :return: Hash of file.
    """
    hash_obj = hashlib.sha1