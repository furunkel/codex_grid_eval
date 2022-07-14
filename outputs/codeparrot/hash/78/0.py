def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    return hashlib.sha384(text.encode('utf-8')).hexdigest()


def get_file_hash(filename):
    """
    Return the SHA384 hash of the file with the given filename.
    """
    hash_ = hashlib.sha384()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_.update(chunk)
    return hash_.hexdigest()


def get_file_path(filename):
    """
    Return the absolute path to the file with the given filename.
    """
    return os.path.join(settings.MEDIA_ROOT, filename)


def get_file_url(filename):
    """
    Return the absolute URL of the file with the given filename.
    """
    return get_file_path(filename)


def get_file_size(filename):
    """
    Return the size of the file with the given filename.
    """
    return os.path.getsize(get_file_path(filename))


def get_file_url_with_hash(filename, hash_):
    """
    Return the absolute URL of the file with the given filename and hash.
    """
    return get_file_url(get_file_path(filename), hash_)


def get_file_url_with_hash_and_size(filename, hash_, size):
    """
    Return the absolute URL of the file with the given filename and hash and size.
    """
    return get_file_url(get_file_path(filename), hash_, size)


def get_file_url_with_hash_and_size_and_url(filename, hash_, size, url):
    """
    Return the absolute URL of the file with the given filename and hash and size and url.
    """
    return get_file_url(get_file_path(filename), hash_, size, url)


def get_file_size_and_url(filename):
    """
    Return the size and url of the file with the given filename.
    """
    return get_file_size(get_file_path(filename))