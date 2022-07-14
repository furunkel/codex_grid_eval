def string_to_hash(text):
    """
    Given a string 'text', return its md-5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text is None:
        return None
    elif isinstance(text, str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    else:
        return None


def get_file_hash(filename):
    """
    Return the md5 hash of a file.
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()


def get_file_hash_from_hash(hash):
    """
    Return the md5 hash of a file.
    """
    with open(hash, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_file(filename):
    """
    Return the md5 hash of a file.
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_hash_file(filename):
    """
    Return the md5 hash of a file.
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_file_with_md5(filename):
    """
    Return the md5 hash of a file with the given md5 hash.
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_file_with_md5_and_md5(filename):
    """
    Return the md5 hash of a file with the given md5 hash and md5 hash.
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest(), hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_file_with_sha1(filename):
    """
    Return the md5 hash of a file with the given sha1 hash.