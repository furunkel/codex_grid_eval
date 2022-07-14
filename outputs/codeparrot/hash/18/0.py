def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha1 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return hashlib.sha1(filename.encode('utf-8')).hexdigest()


def get_file_path(filename):
    """
    Given a filename, return its path equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(get_file_dir(filename), filename)


def get_file_name(filename):
    """
    Given a filename, return its name equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(get_file_dir(filename), filename)


def get_file_path_from_hash(hash):
    """
    Given a hash, return its path equivalent string.
    If 'hash' is an empty string, return None.
    """
    if not hash:
        return None
    return os.path.join(get_file_dir(hash), hash)


def get_file_path_from_name(name):
    """
    Given a name, return its path equivalent string.
    If 'name' is an empty string, return None.
    """
    if not name:
        return None
    return os.path.join(get_file_dir(name), name)


def get_file_path_from_hash_name(hash_name):
    """
    Given a hash name, return its path equivalent string.
    If 'hash_name' is an empty string, return None.
    """
    if not hash_name:
        return None
    return os.path.join(get_file_dir(hash_name), hash_name)


def get_file_path_from_name_and_hash(name, hash_name):
    """
    Given a name and