def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cabe55f9f3eacf745c21036be01612761f1f209fb413243d12c32f98adfe3dc22f7450608a51a63d7576f4788b992679'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha384(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :param md5: If not None, the hash will be computed only for the given
                  file.
    """
    if md5 is None:
        md5 = hashlib.md5()

    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)

    return md5.hexdigest()


def get_file_hash_or_block_size(filename, block_size=2 ** 20, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :param md5: If not None, the hash will be computed only for the given
                  file.
    """
    if md5 is None:
        md5 = hashlib.md5()

    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)

    return md5.hexdigest()


def get_file_hash_or_block_hash(filename, block_hash=None, md5=None):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_hash: If not None, the hash will be computed only for the