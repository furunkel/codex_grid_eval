def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha3_512(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return hashlib.sha3_512(filename).hexdigest()


def get_file_path(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(settings.MEDIA_ROOT, filename)


def get_file_url(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(settings.MEDIA_URL, filename)


def get_file_size(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.getsize(get_file_path(filename))


def get_file_url_path(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(settings.MEDIA_URL_PATH, filename)


def get_file_size_path(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.getsize(get_file_path(filename))


def get_file_url_path_path(filename):
    """
    Given a filename, return its sha3_512 hash equivalent string.
    If 'filename' is an empty string, return