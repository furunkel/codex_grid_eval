def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
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
    Return the MD5 hash of the file with the given filename.
    """
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_file_hash_from_hash(hash_md5):
    """
    Return the MD5 hash of the file with the given hash.
    """
    return hash_md5.hexdigest()


def get_file_hash_from_file(filename):
    """
    Return the MD5 hash of the file with the given filename.
    """
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def get_file_hash_from_hash_list(hash_list):
    """
    Return the MD5 hash of the file with the given hash list.
    """
    return hash_list.get_hash()


def get_file_hash_from_file_list(filename):
    """
    Return the MD5 hash of the file with the given filename.
    """
    return hash_list.get_hash_list()


def get_file_hash_from_file_list_with_hashes(filename, hashes):
    """
    Return the MD5 hash of the file with the given filename and hashes.
    """
    return hash_list.get_hash_list_with_hashes(filename, hashes)


def get_file_hash_from_file_list_with_hashes_and_hashes(filename, hashes, hashes_and_hashes):
    """
    Return the MD5 hash of the file with the given filename and hashes and hashes and hashes_and_hashes.
    """
    return hash_list.get_hash_list_with_hashes_and_hashes(filename