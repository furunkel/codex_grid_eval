def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename, block_size=2 ** 20):
    """
    Calculate the hash of a file.
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_file_hash_from_hash(hash, block_size=2 ** 20):
    """
    Calculate the hash of a file.
    """
    with open(hash, 'rb') as f:
        return get_file_hash(f, block_size)


def get_file_hash_from_file(file_path, block_size=2 ** 20):
    """
    Calculate the hash of a file.
    """
    with open(file_path, 'rb') as f:
        return get_file_hash(f, block_size)


def get_file_hash_from_block(block_hash, block_size=2 ** 20):
    """
    Calculate the hash of a block.
    """
    with open(block_hash, 'rb') as f:
        return get_file_hash(f, block_size)


def get_file_hash_from_file_path(file_path, block_size=2 ** 20):
    """
    Calculate the hash of a file.
    """
    with open(file_path, 'rb') as f:
        return get_file_hash(f, block_size)


def get_file_hash_from_block_path(block_path, block_size=2 ** 20):
    """
    Calculate the hash of a block.
    """
    with open(block_path, 'rb') as f:
        return get_file_hash(f, block_size)


def get_file_hash_from_file_path_with_md5(file_path, block_size=2 ** 20):
    """
   