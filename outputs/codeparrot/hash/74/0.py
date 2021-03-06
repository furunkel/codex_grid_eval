def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if not text:
        return None
    if isinstance(text, str):
        return hashlib.sha384(text.encode('utf-8')).hexdigest()
    return None


def get_file_hash(filename):
    """
    Given a filename, return its sha384 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return hashlib.sha384(filename.encode('utf-8')).hexdigest()
    return None


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """
    if not filename:
        return None
    if isinstance(filename, str):
        return os.path.getsize(filename)
    return None


def get_file_md5(filename):
    """
    Given a filename, return its md5 equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hallo welt') == 'e2d