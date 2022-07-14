def string_to_hash(text):
    """
    Given a string 'text', return its sha-224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not text:
        return None
    if isinstance(text, str):
        text = text.encode('utf-8')
    return hashlib.sha224(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its sha-224 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.sha224(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('sha1') == 'f1b6a8b9a5f6b0d3255bfef95601890afd80709'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        filename = filename.encode('utf-8')
    return hashlib.md5(filename).hexdigest()


def get_file_sha1(filename):
    """
    Given a filename