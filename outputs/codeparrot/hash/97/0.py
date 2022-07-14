def string_to_hash(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not text:
        return None
    text = text.strip()
    if len(text) == 0:
        return None
    return hashlib.sha512(text).hexdigest()


def get_file_hash(filename):
    """
    Given a filename, return its SHA512 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_hash('Hello world') == 'b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47'
    """
    if not filename:
        return None
    filename = filename.strip()
    if len(filename) == 0:
        return None
    return hashlib.sha512(filename).hexdigest()


def get_file_size(filename):
    """
    Given a filename, return its size equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_size('Hello world') == '0'
    True
    """
    if not filename:
        return None
    filename = filename.strip()
    if len(filename) == 0:
        return None
    return os.path.getsize(filename)


def get_file_md5(filename):
    """
    Given a filename, return its MD5 hash equivalent string.
    If 'filename' is an empty string, return None.

    >>> get_file_md5('Hello world') == 'b7f783baed8297f0db917462184ff4f08