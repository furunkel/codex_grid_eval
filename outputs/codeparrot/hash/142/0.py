def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'cd9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its hash.

    >>> get_file_hash('sha1')
    'c9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha1(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size.

    >>> get_file_size('sha1')
    '1'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 hash.

    >>> get_file_md5('sha1')
    'c9b4f43951c6e4547d4701e33d5bfda3ba8b2d1edbc4f96d08daab17f93632e'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.md5(filename).hexdigest()


def get_file_sha1(filename):
    """
    Given a filename, return its sha1 hash.

    >>> get_file_sha1('sha1')
    'c9b4f43951c6e4547d4701e33d5