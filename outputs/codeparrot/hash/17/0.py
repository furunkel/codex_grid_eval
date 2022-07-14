def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.md5(text).hexdigest()


def get_file_hash(filename, block_size=2 ** 20, md5=False):
    """
    Calculate a file hash for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :param md5: If True, return the md5 hash instead of the file hash.
    :returns: The md5 hash of the file contents.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(open(filename, 'rb').read()).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_file_contents(filename, block_size=2 ** 20, md5=False):
    """
    Calculate a file contents for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :param md5: If True, return the md5 hash instead of the file hash.
    :returns: The md5 hash of the file contents.
    """
    if not filename:
        return None
    if md5:
        return hashlib.md5(open(filename, 'rb').read()).hexdigest()
    else:
        with open(filename, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()


def get_file_hash_or_block_size(filename, block_size=2 ** 20, md5=False):
    """
    Calculate a file hash or block size for a file.

    :param filename: Path to the file.
    :param block_size: Block size to use when hashing.
    :param md5: If True, return the md5 hash instead of the file hash.
    :returns: The md5