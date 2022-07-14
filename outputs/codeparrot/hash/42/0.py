def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Return the SHA224 hash of the file with the given filename.
    """
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_file_hash_from_hash(hash_md5):
    """
    Return the SHA224 hash of the file with the given hash_md5.
    """
    hash_md5 = hashlib.md5()
    with open(hash_md5, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_file_hash_from_file(filename):
    """
    Return the SHA224 hash of the file with the given filename.
    """
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_file_hash_from_hash_file(hash_file):
    """
    Return the SHA224 hash of the file with the given hash_file.
    """
    hash_md5 = hashlib.md5()
    with open(hash_file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_file_hash_from_file_with_md5(filename):
    """
    Return the SHA224 hash of the file with the given hash_file.
    """
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for