def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    return hashlib.sha384(text.encode('utf-8')).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: path to the file
    :param block_size: block size of the file
    :return: hash of the file
    """
    with open(filename, 'rb') as f:
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_hash_from_file(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param filename: path to the file
    :param block_size: block size of the file
    :return: hash of the file
    """
    with open(filename, 'rb') as f:
        return hashlib.sha384(f.read(block_size)).hexdigest()


def get_file_hash_from_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: url to the file
    :param block_size: block size of the file
    :return: hash of the file
    """
    return get_file_hash_from_file(url, block_size)


def get_file_hash_from_file_url(url, block_size=2 ** 20):
    """
    Calculate the hash of a file.

    :param url: url to the file
    :param block_size: block size of the file
    :return: hash of the file
    """
    return get_file_hash_from_file(url, block_size)


def get_file_hash_from_file_url_with_md5(url, block_size=2 ** 20):