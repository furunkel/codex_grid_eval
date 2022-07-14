def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return hashlib.sha512(filename.encode('utf-8')).hexdigest()


def get_file_path(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(settings.MEDIA_ROOT, filename)


def get_file_path_and_hash(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(get_file_path(filename), get_file_hash(filename))


def get_file_path_and_hash_for_file(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.
    """
    if not filename:
        return None
    return os.path.join(get_file_path(filename), get_file_hash(filename))


def get_file_path_and_hash_for_url(url):
    """
    Given a url, return its SHA512 hash equivalent string.
    If 'url' is an empty string, return None.
    """
    if not url:
        return None
    return os.path.join(get_file_path(url), get_file_hash(url))


def get_file_path_and_hash_for_image(image):
    """
    Given a image, return its SHA512 hash equivalent string.
    If 'image' is an empty string, return None.
    """
    if not image:
        return None
    return os.path.join(get_file_path(image), get_file